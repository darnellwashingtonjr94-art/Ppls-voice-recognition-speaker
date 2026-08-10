#!/bin/bash
# build_pipeline.sh - Orchestrates the full A/V generation sequence

set -e # Exit immediately if a pipeline stage fails

echo "[*] Initializing AI Generation Pipeline..."

echo "[*] Stage 1/4: Executing RVC Voice Cloning..."
python3 rvc_pipeline.py

echo "[*] Stage 2/4: Applying Metallic Vocoder FX..."
python3 vocoder_fx.py # Ensure your python audio processing script is named this

echo "[*] Stage 3/4: Submitting Video Render to Veo API..."
python3 veo_generator.py

echo "[*] Stage 4/4: Muxing Audio & Video Master..."
python3 mux_av.py

echo "[*] Pipeline complete. Production artifacts are ready for deployment."
