import numpy as np
from core import fast_matcher # Custom C++ binding
from models.embeddings import VoiceprintExtractor

class QuantumUnitProcessor:
    def __init__(self):
        self.extractor = VoiceprintExtractor()
        # Initialize the C++ high-speed matching engine
        self.matcher = fast_matcher.VectorEngine()

    def process_and_match(self, clean_audio_path, database_matrix):
        """Extracts frequency embeddings and executes a sub-millisecond match."""
        vector = self.extractor.extract(clean_audio_path).cpu().numpy()
        
        # Offload the heavy matrix multiplication to the C++ AVX-512 engine
        best_idx, confidence = self.matcher.compute_cosine_simd(vector, database_matrix)
        
        return best_idx, confidence

if __name__ == "__main__":
    print("Quantum Unit initialized. DSP and C++ routing active.")
