import torch
import torchaudio
from speechbrain.pretrained import EncoderClassifier

class VoiceprintExtractor:
    def __init__(self, model_source="speechbrain/spkrec-ecapa-voxceleb"):
        """Loads the pretrained ECAPA-TDNN embedding extractor."""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.classifier = EncoderClassifier.from_hparams(
            source=model_source, 
            run_opts={"device": self.device}
        )

    def extract(self, wav_file):
        """Extracts a 192-dimensional vector representing the speaker's voice."""
        signal, fs = torchaudio.load(wav_file)
        embeddings = self.classifier.encode_batch(signal)
        return embeddings.squeeze()
