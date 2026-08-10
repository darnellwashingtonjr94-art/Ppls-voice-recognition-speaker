<div align="center">


<p align="center">
  <img src="IMG_3932.png" alt="Profile Image" width="400"/>
</p>

# 🎼 🌐 Ppls-Voice-Recognition-Speaker

A high-performance, open-source speaker recognition ecosystem optimized for identifying stars, athletes, and crowdsourced voices.

## Badges

| Category | Technologies |
| :--- | :--- |
| **Languages** | ![C++17](https://img.shields.io/badge/c++17-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) ![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white) ![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white) ![Python 3.11](https://img.shields.io/badge/python%203.11-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Solidity](https://img.shields.io/badge/Solidity-%23363636.svg?style=for-the-badge&logo=solidity&logoColor=white) |
| **Systems** | ![AVX-512](https://img.shields.io/badge/AVX--512-blue?style=for-the-badge) ![SIMD](https://img.shields.io/badge/SIMD-blue?style=for-the-badge) ![Pybind11](https://img.shields.io/badge/Pybind11-blue?style=for-the-badge) |
| **Architecture** | ![x86_64](https://img.shields.io/badge/x86__64-gray?style=for-the-badge) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![RunPod GPU](https://img.shields.io/badge/RunPod%20GPU-673AB7?style=for-the-badge) |
| **Performance** | ![Sub-millisecond](https://img.shields.io/badge/Sub--millisecond-brightgreen?style=for-the-badge) ![Zero-Copy Buffers](https://img.shields.io/badge/Zero--Copy%20Buffers-brightgreen?style=for-the-badge) |
| **Security** | ![Bandit](https://img.shields.io/badge/Bandit-red?style=for-the-badge) ![Gosec](https://img.shields.io/badge/Gosec-red?style=for-the-badge) ![EVM Audited](https://img.shields.io/badge/EVM%20Audited-blueviolet?style=for-the-badge) |
| **DevOps** | ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![CMake](https://img.shields.io/badge/CMake-%23008FBA.svg?style=for-the-badge&logo=cmake&logoColor=white) |
| **AI & Audio** | ![SpeechBrain](https://img.shields.io/badge/SpeechBrain-ff69b4?style=for-the-badge) ![ECAPA-TDNN](https://img.shields.io/badge/ECAPA--TDNN-orange?style=for-the-badge) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) |

## Why is this cool?

*   **Blazing Speed & Hardware Optimization:** Leverages C++ AVX-512 intrinsics and Pybind11 to compute vector comparisons at hardware-level speeds.
*   **Multimodal Architecture:** Seamlessly merges machine learning inference, high-concurrency Go ingestion workers, containerized deployment, and decentralized Web3 ledgers.
*   **Studio-Ready Metrics:** Bridges the gap between experimental AI models and real-world audio production tools by tracking plugin latency constraints for industry-standard DAWs like Pro Tools and FL Studio.

## How this works?

1.  **Infiltration & VAD:** Audio files enter through the FastAPI backend or Go ingestion workers, where Voice Activity Detection strips silence and isolates vocal tracts.
2.  **Feature Extraction:** PyTorch and SpeechBrain convert the processed audio slice into a 192-dimensional vector embedding.
3.  **SIMD Matching:** The query vector is passed to the execution layer to perform fast cosine similarity comparisons against database matrices using AVX-512 SIMD instructions.

## System Architecture

This repository operates across three distinct layers to ensure maximum throughput and security:

1. **AI & DSP Layer (Python 3.11)**
   *   `src/quantum_unit.py` manages audio ingestion and routes signals to PyTorch/SpeechBrain.
   *   Outputs a 192-dimensional vector embedding.

2. **Execution Layer (C++ 17 / AVX-512)**
   *   `core/vector_engine.cpp` bypasses Python's GIL for heavy matrix multiplication.
   *   Executes 1:N cosine similarity searches across millions of cached voiceprints in sub-millisecond timeframes.

3. **Consensus Layer (Solidity)**
   *   `contracts/VoiceRegistry.sol` provides immutable anchoring.
   *   Hashed embeddings are stored on-chain to provide zero-knowledge proof of voice authentication without leaking biometric data.
