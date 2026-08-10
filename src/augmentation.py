import torch
import torchaudio
import random

class EnvironmentalAugmentation:
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate
        # Example impulse responses for stadium/room reverb
        self.reverb = torchaudio.transforms.Vol(gain=1.0) 

    def apply_noise(self, waveform, snr_db=15):
        """Injects white noise at a specific Signal-to-Noise Ratio."""
        noise = torch.randn_like(waveform)
        signal_power = waveform.norm(p=2)
        noise_power = noise.norm(p=2)
        
        scale = signal_power / noise_power * (10 ** (-snr_db / 20.0))
        return waveform + noise * scale

    def process(self, waveform):
        """Randomly applies DSP effects for training robustness."""
        if random.random() > 0.5:
            waveform = self.apply_noise(waveform, snr_db=random.randint(5, 20))
        return waveform
