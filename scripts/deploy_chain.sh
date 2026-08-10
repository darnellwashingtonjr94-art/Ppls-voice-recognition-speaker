#!/bin/bash
set -e

echo ">>> Preparing smart contract environment..."

# Ensure we are in the project root
cd "$(dirname "$0")/.."

# Verify Node dependencies are installed
if [ ! -d "node_modules" ]; then
    echo ">>> Installing npm dependencies..."
    npm install
fi

# Ensure the .env file exists for the Monad RPC and Private Key
if [ ! -f ".env" ]; then
    echo "ERROR: .env file missing."
    echo "Please create a .env file with MONAD_RPC_URL and PRIVATE_KEY."
    exit 1
fi

echo ">>> Compiling Solidity contracts..."
npx hardhat compile

echo ">>> Pushing contract to the Monad network..."
npx hardhat run scripts/deploy.js --network monad_testnet

echo ">>> Chain deployment complete."
