import os
from dataclasses import dataclass

@dataclass
class Config:
    # Audio Settings
    SAMPLE_RATE: int = 16000
    
    # Model Settings
    MODEL_HUB: str = "speechbrain/spkrec-ecapa-voxceleb"
    COSINE_THRESHOLD: float = 0.35
    
    # Storage Paths
    RAW_DATA_DIR: str = os.getenv("RAW_DATA_DIR", "data/raw")
    PROCESSED_DATA_DIR: str = os.getenv("PROCESSED_DATA_DIR", "data/processed")
    DB_PATH: str = os.getenv("DB_PATH", "data/voiceprints.db")

cfg = Config()
