import pytest
import torch
from models.embeddings import VoiceprintExtractor

@pytest.fixture
def extractor():
    return VoiceprintExtractor()

def test_embedding_dimensions(extractor):
    """
    Ensures the PyTorch model outputs a 192-dimensional vector. 
    If this fails, the model architecture was altered and breaks the database schema.
    """
    # Create a fake 3-second audio tensor at 16kHz
    dummy_audio = torch.randn(1, 48000) 
    
    # Bypass file loading for the test, test the raw encoding batch
    embeddings = extractor.classifier.encode_batch(dummy_audio)
    
    assert embeddings.shape[-1] == 192, f"Expected 192 dimensions, got {embeddings.shape[-1]}"
