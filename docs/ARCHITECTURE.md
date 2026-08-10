# System Architecture

This repository operates across three distinct layers to ensure maximum throughput and security:

1. **AI & DSP Layer (Python 3.11)**
   - `src/quantum_unit.py` manages audio ingestion and routes signals to PyTorch/SpeechBrain.
   - Outputs a 192-dimensional vector embedding.
   
2. **Execution Layer (C++ 17 / AVX-512)**
   - `core/vector_engine.cpp` bypasses Python's GIL for heavy matrix multiplication.
   - Executes 1:N cosine similarity searches across millions of cached voiceprints in sub-millisecond timeframes.
   
3. **Consensus Layer (Solidity)**
   - `contracts/VoiceRegistry.sol` provides immutable anchoring.
   - Hashed embeddings are stored on-chain to provide zero-knowledge proof of voice authentication without leaking biometric data.
