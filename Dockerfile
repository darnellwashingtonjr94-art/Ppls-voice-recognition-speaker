FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for audio processing
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download models to bake them into the image
RUN python -c "from silero_vad import load_silero_vad; load_silero_vad()"
RUN python -c "from speechbrain.pretrained import EncoderClassifier; EncoderClassifier.from_hparams(source='speechbrain/spkrec-ecapa-voxceleb')"

COPY . .

EXPOSE 8000
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
