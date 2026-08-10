import os
import torchaudio
import torch
from pathlib import Path

def format_audio(input_file, output_file, target_sr=16000):
    """Converts audio to WAV and resamples to 16kHz."""
    waveform, sample_rate = torchaudio.load(input_file)
    
    if sample_rate != target_sr:
        resampler = torchaudio.transforms.Resample(sample_rate, target_sr)
        waveform = resampler(waveform)
    
    # Convert stereo to mono if needed
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)
    
    torchaudio.save(output_file, waveform, target_sr)
    print(f"Formatted: {output_file}")

if __name__ == "__main__":
    print("Preprocessing engine initialized. Ready for batch formatting.")
