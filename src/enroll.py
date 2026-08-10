import argparse
from src.vad import VoiceActivityDetector
from models.embeddings import VoiceprintExtractor
from src.database import VoiceprintDatabase
import os

def enroll_speaker(name, category, audio_path):
    vad = VoiceActivityDetector()
    extractor = VoiceprintExtractor()
    db = VoiceprintDatabase()

    print(f"Enrolling {name} ({category})...")
    
    # 1. Strip silence
    clean_audio = f"/tmp/{name}_clean.wav"
    vad.remove_silence(audio_path, clean_audio)
    
    # 2. Extract mathematical vector
    vector = extractor.extract(clean_audio).cpu().numpy()
    
    # 3. Save to DB
    db.insert_speaker(name, category, vector)
    print("Enrollment successful.")
    
    os.remove(clean_audio)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True, type=str)
    parser.add_argument('--category', required=True, choices=['star', 'athlete', 'public'])
    parser.add_argument('--audio', required=True, type=str)
    
    args = parser.parse_args()
    enroll_speaker(args.name, args.category, args.audio)
