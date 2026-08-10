import time
import torch
from models.embeddings import VoiceprintExtractor

def run_latency_test(iterations=1000):
    extractor = VoiceprintExtractor()
    dummy_tensor = torch.randn(1, 48000).to(extractor.device) # 3 seconds of audio
    
    print(f"Warming up GPU for {iterations} iterations...")
    for _ in range(10):
        _ = extractor.classifier.encode_batch(dummy_tensor)
        
    start = time.perf_counter()
    for _ in range(iterations):
        _ = extractor.classifier.encode_batch(dummy_tensor)
    end = time.perf_counter()
    
    avg_ms = ((end - start) / iterations) * 1000
    print(f"Average Inference Latency: {avg_ms:.3f} ms per 3-second audio clip")

if __name__ == "__main__":
    run_latency_test()
