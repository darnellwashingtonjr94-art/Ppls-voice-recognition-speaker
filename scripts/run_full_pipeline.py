import subprocess
import sys
import os

def run_command(command, description):
    print(f"\n[PHASE] {description}...")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Failed during: {description}")
        sys.exit(1)
    print(f"[SUCCESS] {description} completed.")

if __name__ == "__main__":
    print("=== STARTING FULL MASTER PIPELINE INTEGRATION ===")
    
    # 1. Compile C++ AVX-512 Engine via script wrapper
    run_command("./scripts/build_engine.sh", "Compiling C++ SIMD Vector Engine")
    
    # 2. Run Accuracy and Metrics Evaluation Suite
    run_command("python3.11 src/accuracy_metrics.py", "Running Biometric Accuracy Metrics")
    
    # 3. Run DAW Telemetry Verification (FL Studio & Pro Tools)
    run_command("python3.11 src/daw_telemetry.py", "Validating DAW Audio Buffer Performance")
    
    # 4. Run Pytest Suite
    run_command("pytest tests/ -v", "Executing Test Suite")
    
    print("\n=== ALL SYSTEMS OPERATIONAL: CLAUDE & CODEX PIPELINE SYNCED ===")
