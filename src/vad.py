import torch
import torchaudio
from silero_vad import load_silero_vad, get_speech_timestamps, collect_chunks

class VoiceActivityDetector:
    def __init__(self):
        """Loads the ultra-fast, enterprise-grade Silero VAD model."""
        self.model = load_silero_vad()

    def remove_silence(self, wav_path, output_path):
        """Detects human speech and exports a condensed, silence-free WAV."""
        wav, sr = torchaudio.load(wav_path)
        
        # Ensure audio is mono 16kHz for Silero
        if sr != 16000:
            wav = torchaudio.transforms.Resample(sr, 16000)(wav)
        wav = wav.mean(dim=0, keepdim=True) if wav.shape[0] > 1 else wav

        timestamps = get_speech_timestamps(wav, self.model, sampling_rate=16000)
        
        if not timestamps:
            raise ValueError(f"No human speech detected in {wav_path}")

        # Stitch together only the active speech segments
        speech_tensor = collect_chunks(timestamps, wav)
        torchaudio.save(output_path, speech_tensor.unsqueeze(0), 16000)
        return output_path
