# Base image with CUDA support for accelerated audio processing
FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency manifest and install Python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy source scripts into the runtime workspace
COPY . /app/

# Environment variables
ENV PYTHONUNBUFFERED=1

# Entrypoint for job orchestration
CMD ["python3", "deploy_serverless.py"]
