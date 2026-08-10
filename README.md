<div align="center">

IMG_3932.png

# 🎼🌐 Ppls-Voice-Recognition-Speaker

A high-performance, open-source speaker recognition ecosystem optimized for identifying stars, athletes, and crowdsourced voices. 

</div>

---

## Badges

[![Core Programming Languages](https://img.shields.io/badge/Languages-C++17_%7C_Rust_%7C_Go_%7C_Python_3.11_%7C_Solidity-blue.svg)](https://github.com/)
[![Core Systems](https://img.shields.io/badge/Systems-AVX--512_%7C_SIMD_%7C_Pybind11-orange.svg)](https://github.com/)
[![Platform Support & Hardware Architecture](https://img.shields.io/badge/Architecture-x86__64_%7C_Linux_%7C_RunPod_GPU-informational.svg)](https://github.com/)
[![Low-Level Infrastructure & Performance](https://img.shields.io/badge/Performance-Sub--millisecond_%7C_Zero--Copy_Buffers-success.svg)](https://github.com/)
[![Cybersecurity & Offensive Auditing](https://img.shields.io/badge/Security-Bandit_%7C_Gosec_%7C_EVM_Audited-critical.svg)](https://github.com/)
[![DevOps & Build Tools](https://img.shields.io/badge/DevOps-GitHub_Actions_%7C_Terraform_%7C_Docker_%7C_CMake-yellow.svg)](https://github.com/)
[![Artificial Intelligence & Quantum](https://img.shields.io/badge/AI_%26_Audio-SpeechBrain_%7C_ECAPA--TDNN_%7C_PyTorch_%7C_FastAPI-purple.svg)](https://github.com/)
[![Cloud Providers](https://img.shields.io/badge/Cloud-AWS_%7C_RunPod_%7C_EVM_Monad-blueviolet.svg)](https://github.com/)

---

## What is this about?
This project is an end-to-end multimodal speaker identification framework. It combines deep learning acoustic voice fingerprinting, a lightning-fast C++ SIMD hardware-accelerated search engine, decentralized identity anchoring via smart contracts, and professional-grade audio monitoring telemetry tailored for studio recording environments.

## What this does?
* **Voice Ingestion & Preprocessing:** Cleans, normalizes, and removes silence from raw audio inputs using Silero VAD and Torchaudio.
* **Deep Embedding Extraction:** Generates robust 192-dimensional voiceprints using SpeechBrain's ECAPA-TDNN architecture.
* **High-Speed Matching:** Executes $1:N$ vector similarity searches bypassing Python's Global Interpreter Lock (GIL) utilizing a vectorized C++17 AVX-512 backend (`fast_matcher`).
* **Blockchain Verification:** Anchors cryptographic voice hashes immutably onto EVM-compatible networks (such as Monad) to ensure zero-knowledge proof of identity.
* **DAW Telemetry & Reasoning:** Monitors processing block latency against strict FL Studio and Pro Tools hardware buffer limits, alongside Google Gemini-powered reasoning modules for resolving ambiguous matches.

## Why is this cool?
* **Blazing Speed & Hardware Optimization:** Leverages C++ AVX-512 intrinsics and Pybind11 to compute vector comparisons at hardware-level speeds.
* **Multimodal Architecture:** Seamlessly merges machine learning inference, high-concurrency Go ingestion workers, containerized deployment, and decentralized Web3 ledgers.
* **Studio-Ready Metrics:** Bridges the gap between experimental AI models and real-world audio production tools by tracking plugin latency constraints for industry-standard DAWs like Pro Tools and FL Studio.

## How this works?
1. **Infiltration & VAD:** Audio files enter through the FastAPI backend or Go ingestion workers, where Voice Activity Detection strips silence and isolates vocal tracts.
2. **Feature Extraction:** PyTorch and SpeechBrain convert the processed audio slice into a 192-dimensional vector embedding.
3. **SIMD Matching:** The query vector is passed through Pybind11 to the C++ core engine (`vector_engine.cpp`), which scans database matrices using AVX-512 SIMD parallelism to find the closest match.
4. **Validation & Anchoring:** Results are evaluated via metric thresholds or passed to Gemini for reasoning, optionally anchoring the identity hash to the `VoiceRegistry.sol` smart contract.

## What problems this solves?
* **High-Latency Voice Recognition:** Eliminates the slowness of pure Python tensor loop calculations by offloading heavy matrix math to optimized C++ SIMD routines.
* **Identity Spoofing & Tampering:** Resolves trust and verification issues in digital media by immutably anchoring voice hashes to blockchain ledgers.
* **DAW Integration Blind Spots:** Solves the lack of performance visibility when running heavy AI audio plugins inside real-time music production environments.

## What problems this creates for people and businesses?
* **Hardware Dependencies:** The C++ vector engine relies heavily on AVX-512 instruction sets, meaning older CPU architectures will face compatibility issues or degraded performance fallback.
* **Privacy & Surveillance Risks:** Deploying high-accuracy speaker recognition across public figures, athletes, and crowdsourced voices raises significant biometric tracking and privacy concerns.
* **Infrastructure Complexity:** Maintaining a multi-stack ecosystem (Python, C++, Go, Solidity, Terraform, and Docker) creates heavy maintenance overhead for engineering teams.

## How to install this?

To initialize the environment, build the C++ engine, and install all python dependencies automatically, run the master initialization script:

```bash
chmod +x scripts/*.sh
./scripts/init_all.sh
