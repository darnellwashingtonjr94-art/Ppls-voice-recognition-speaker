import torch
from models.embeddings import VoiceprintExtractor

def compare_voices(wav_file_1, wav_file_2, threshold=0.25):
    """Compares two audio files to determine if they are the same person."""
    extractor = VoiceprintExtractor()
    
    emb1 = extractor.extract(wav_file_1)
    emb2 = extractor.extract(wav_file_2)
    
    # Calculate how similar the two mathematical vectors are
    similarity = torch.nn.functional.cosine_similarity(emb1.unsqueeze(0), emb2.unsqueeze(0))
    score = similarity.item()
    
    is_match = score > threshold
    return is_match, score

if __name__ == "__main__":
    print("Inference module ready.")
