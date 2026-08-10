import sys
import speechbrain as sb
from hyperpyyaml import load_hyperpyyaml

class SpeakerRecognitionBrain(sb.Brain):
    def compute_forward(self, batch, stage):
        """Forward pass through the neural network."""
        batch = batch.to(self.device)
        wavs, lens = batch.sig
        feats = self.hparams.compute_features(wavs)
        feats = self.modules.mean_var_norm(feats, lens)
        embeddings = self.modules.embedding_model(feats)
        outputs = self.modules.classifier(embeddings)
        return outputs

    def compute_objectives(self, predictions, batch, stage):
        """Calculates loss during training."""
        _, lens = batch.sig
        spkid, _ = batch.spk_id_encoded
        loss = self.hparams.compute_cost(predictions, spkid, lens)
        return loss

if __name__ == "__main__":
    print("Trainer requires hparams.yaml to execute.")
