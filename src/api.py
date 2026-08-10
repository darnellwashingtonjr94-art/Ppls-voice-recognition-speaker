from fastapi import FastAPI, UploadFile, File
import torch
import numpy as np
from models.embeddings import VoiceprintExtractor
from src.database import VoiceprintDatabase
from src.vad import VoiceActivityDetector
import shutil

app = FastAPI(title="Voice Recognition Engine")

extractor = VoiceprintExtractor()
db = VoiceprintDatabase()
vad = VoiceActivityDetector()

@app.post("/identify")
async def identify_speaker(file: UploadFile = File(...)):
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        clean_path = f"/tmp/clean_{file.filename}"
        vad.remove_silence(temp_path, clean_path)
        
        query_vector = extractor.extract(clean_path).cpu()
        metadata, db_vectors = db.get_all_embeddings()
        
        db_tensor = torch.tensor(db_vectors)
        
        # Matrix multiplication for ultra-fast cosine similarity across the entire DB
        similarities = torch.nn.functional.cosine_similarity(query_vector.unsqueeze(0), db_tensor)
        
        best_match_idx = torch.argmax(similarities).item()
        confidence = similarities[best_match_idx].item()
        
        if confidence > 0.35: # General threshold for ECAPA-TDNN
            return {"match": metadata[best_match_idx], "confidence": confidence}
        return {"match": "Unknown", "confidence": confidence}
        
    finally:
        # Cleanup logic would go here
        pass
