"""Smoke test VieNeu-TTS v3 Turbo on this Mac (ONNX/CPU)."""
from time import time
from pathlib import Path

from vieneu import Vieneu

out_dir = Path(__file__).resolve().parent
print("Loading VieNeu-TTS v3 Turbo (ONNX/CPU, 48 kHz)...")
t0 = time()
tts = Vieneu()
print(f"Loaded in {time() - t0:.1f}s")

voices = tts.list_preset_voices()
print(f"\n{len(voices)} preset voices:")
for label, voice_id in voices:
    print(f"  - {label} ({voice_id})")

text = "Xin chào. Đây là bài kiểm tra VieNeu TTS phiên bản ba Turbo trên máy Mac."
print(f"\nGenerating:\n  {text}")
start = time()
audio = tts.infer(text)
elapsed = time() - start

out_path = out_dir / "smoke_minh_quan.wav"
tts.save(audio, str(out_path))

sr = 48000
duration = len(audio) / sr
rtf = elapsed / duration if duration else 0
print(f"\nSaved: {out_path}")
print(f"Audio duration: {duration:.2f}s")
print(f"Wall time:      {elapsed:.2f}s")
print(f"RTF:            {rtf:.3f} ({1/rtf:.2f}x real-time)" if rtf else "")
print("OK")
