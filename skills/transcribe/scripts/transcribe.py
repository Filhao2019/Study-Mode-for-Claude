#!/usr/bin/env python3
"""Transcribe a lecture recording on this computer with Whisper.

Nothing is uploaded: the model runs locally. Uses faster-whisper when it is
installed (quicker, lighter) and falls back to openai-whisper.

Writes, next to each other:
  <name>.md    timestamped paragraphs, "[00:12:34] ...", ready for notes
  <name>.srt   subtitles, to check the text against the recording
  <name>.json  raw segments with start and end times

Usage:
  python transcribe.py lecture.m4a --id S7 --title "Lecture 5" --out-dir study/bio-101/sources
  python transcribe.py lecture.mp4 --model medium --language pt

Install one engine first:
  pip install faster-whisper          (recommended; reads audio and video directly)
  pip install openai-whisper          (also needs ffmpeg on your PATH)

Exit codes: 0 success, 1 error, 2 no Whisper engine installed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
import time
from pathlib import Path

NO_ENGINE = 2
VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
MODELS = "tiny, base, small, medium, large-v3 (any name your Whisper engine supports)"


def stamp(seconds: float, srt: bool = False) -> str:
    millis = int(round(seconds * 1000))
    hours, rest = divmod(millis, 3_600_000)
    minutes, rest = divmod(rest, 60_000)
    secs, millis = divmod(rest, 1000)
    if srt:
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def run_faster_whisper(path: Path, args) -> tuple[list[dict], dict]:
    from faster_whisper import WhisperModel  # type: ignore

    device = args.device
    if device == "auto":
        try:
            import ctranslate2  # type: ignore

            device = "cuda" if ctranslate2.get_cuda_device_count() > 0 else "cpu"
        except Exception:
            device = "cpu"

    def transcribe_on(device: str):
        compute_type = "float16" if device == "cuda" else "int8"
        print(f"Loading faster-whisper '{args.model}' on {device} ({compute_type})...", file=sys.stderr)
        model = WhisperModel(args.model, device=device, compute_type=compute_type)
        segments_iter, info = model.transcribe(str(path), language=args.language, vad_filter=True, beam_size=5)
        segments, next_report = [], 60.0
        for segment in segments_iter:  # decoding happens lazily, while iterating
            segments.append({"start": segment.start, "end": segment.end, "text": segment.text.strip()})
            if segment.end >= next_report:
                print(f"  ... {stamp(segment.end)} of {stamp(info.duration)}", file=sys.stderr)
                next_report += 60.0
        return segments, info

    try:
        segments, info = transcribe_on(device)
    except Exception as exc:
        # A GPU is often detected while its CUDA libraries (cuBLAS, cuDNN) are missing; the CPU always works.
        if device != "cuda" or args.device == "cuda" or not re.search(r"cuda|cublas|cudnn|gpu", str(exc), re.I):
            raise
        print(f"GPU not usable ({exc}). Falling back to the CPU.", file=sys.stderr)
        segments, info = transcribe_on("cpu")
    meta = {
        "engine": f"faster-whisper {args.model}",
        "language": f"{info.language} ({info.language_probability:.2f})",
        "duration": stamp(info.duration),
    }
    return segments, meta


def run_openai_whisper(path: Path, args) -> tuple[list[dict], dict]:
    import whisper  # type: ignore

    if shutil.which("ffmpeg") is None:
        raise RuntimeError("openai-whisper needs ffmpeg on your PATH. Install ffmpeg, or use "
                           "'pip install faster-whisper', which doesn't need it.")
    device = None if args.device == "auto" else args.device
    print(f"Loading openai-whisper '{args.model}'...", file=sys.stderr)
    model = whisper.load_model(args.model, device=device)
    fp16 = getattr(model, "device", None) is not None and str(model.device).startswith("cuda")
    result = model.transcribe(str(path), language=args.language, fp16=fp16, verbose=False)
    segments = [{"start": s["start"], "end": s["end"], "text": s["text"].strip()} for s in result["segments"]]
    meta = {
        "engine": f"openai-whisper {args.model}",
        "language": result.get("language") or (args.language or "unknown"),
        "duration": stamp(segments[-1]["end"] if segments else 0),
    }
    return segments, meta


def paragraphs(segments: list[dict], target_seconds: float) -> list[tuple[float, str]]:
    """Group segments into readable paragraphs of about target_seconds each."""
    result, start, parts, last_end = [], None, [], 0.0
    for segment in segments:
        text = segment["text"]
        if not text:
            continue
        long_pause = start is not None and segment["start"] - last_end > 2.5
        if long_pause and parts:
            result.append((start, " ".join(parts)))
            start, parts = None, []
        if start is None:
            start = segment["start"]
        parts.append(text)
        last_end = segment["end"]
        elapsed = segment["end"] - start
        if (elapsed >= target_seconds and re.search(r"[.!?…]$", text)) or elapsed >= 2 * target_seconds:
            result.append((start, " ".join(parts)))
            start, parts = None, []
    if parts:
        result.append((start or 0.0, " ".join(parts)))
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Transcribe a lecture recording locally with Whisper.")
    parser.add_argument("input", help="Audio or video file (.mp3 .m4a .wav .ogg .flac .mp4 .mov .mkv .webm ...)")
    parser.add_argument("--model", default="small", help=f"Whisper model size: {MODELS}. Default: small")
    parser.add_argument("--language", default=None, help="Spoken language code (en, pt, es, ...). Default: detect")
    parser.add_argument("--engine", choices=["auto", "faster", "openai"], default="auto")
    parser.add_argument("--device", choices=["auto", "cpu", "cuda"], default="auto")
    parser.add_argument("--out-dir", default=None, help="Folder for the outputs. Default: next to the input")
    parser.add_argument("--name", default=None, help="Base file name for the outputs. Default: input name")
    parser.add_argument("--id", default="S?", help="Source ID for the Markdown header, e.g. S7")
    parser.add_argument("--title", default=None, help="Title for the Markdown header")
    parser.add_argument("--paragraph-seconds", type=float, default=30.0, help="Target paragraph length. Default: 30")
    args = parser.parse_args(argv)

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    path = Path(args.input)
    if not path.is_file():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    engines = []
    if args.engine in ("auto", "faster"):
        engines.append(("faster-whisper", "faster_whisper", run_faster_whisper))
    if args.engine in ("auto", "openai"):
        engines.append(("openai-whisper", "whisper", run_openai_whisper))

    runner = None
    for package, module, function in engines:
        try:
            __import__(module)
            runner = function
            break
        except ImportError:
            continue
    if runner is None:
        wanted = " or ".join(package for package, _, _ in engines)
        print(f"No Whisper engine found ({wanted}). Install one, for example:\n"
              f"    pip install {engines[0][0]}", file=sys.stderr)
        return NO_ENGINE

    began = time.time()
    try:
        segments, meta = runner(path, args)
    except Exception as exc:
        print(f"Transcription failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    if not segments:
        print("Whisper found no speech in this file. Check that it has audible speech.", file=sys.stderr)
        return 1

    out_dir = Path(args.out_dir) if args.out_dir else path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    base = args.name or path.stem
    title = args.title or f"{path.stem} (transcript)"
    source_type = "video" if path.suffix.lower() in VIDEO_EXTENSIONS else "audio"

    header = [
        "---",
        f"source_id: {args.id}",
        f"title: {title}",
        f"original: {path.as_posix()}",
        f"type: {source_type}",
        f"duration: {meta['duration']}",
        f"language: {meta['language']}",
        f"engine: {meta['engine']}",
        f"transcribed: {dt.date.today().isoformat()}",
        "---",
        "",
        f"# {args.id} · {title}",
        "",
        "> Automatic transcript. Names, numbers, formulas and technical terms can be misheard: "
        "check them against the recording before relying on them.",
        "",
    ]
    body = [f"[{stamp(start)}] {text}" for start, text in paragraphs(segments, args.paragraph_seconds)]
    md_path = out_dir / f"{base}.md"
    md_path.write_text("\n".join(header) + "\n" + "\n\n".join(body) + "\n", encoding="utf-8")

    srt_lines = []
    for number, segment in enumerate(segments, start=1):
        srt_lines += [str(number), f"{stamp(segment['start'], True)} --> {stamp(segment['end'], True)}",
                      segment["text"], ""]
    (out_dir / f"{base}.srt").write_text("\n".join(srt_lines), encoding="utf-8")

    (out_dir / f"{base}.json").write_text(
        json.dumps({"source_id": args.id, "file": path.as_posix(), **meta, "segments": segments},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Done in {time.time() - began:.0f}s: {len(segments)} segments, {meta['duration']} of audio, "
          f"language {meta['language']}.", file=sys.stderr)
    print(f"Wrote {md_path}, {base}.srt and {base}.json in {out_dir}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
