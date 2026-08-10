#!/bin/bash
set -e

echo "=== INITIALIZING PPLS-VOICE-RECOGNITION-SPEAKER ==="

# 1. Make all scripts executable
chmod +x scripts/*.sh

# 2. Build the high-performance C++ matching engine
./scripts/build_engine.sh

# 3. Setup Python 3.11 environment and dependencies
echo ">>> Setting up Python dependencies..."
python3.11 -m pip install -r requirements.txt

# 4. Deploy the smart contract layer
./scripts/deploy_chain.sh

echo "=== SYSTEM INITIALIZATION COMPLETE ==="
