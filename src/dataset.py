import os
import csv
from pathlib import Path

def generate_speechbrain_csv(data_dir, output_csv):
    """
    Scans the processed audio directory and generates a SpeechBrain-compliant CSV.
    Expected structure: data/processed/{speaker_id}/{video_id}/{audio.wav}
    """
    data_dir = Path(data_dir)
    csv_data = []

    for speaker_dir in data_dir.iterdir():
        if not speaker_dir.is_dir():
            continue
        
        spk_id = speaker_dir.name
        for audio_file in speaker_dir.rglob('*.wav'):
            # The ID must be a unique identifier for the utterance
            utt_id = f"{spk_id}_{audio_file.stem}"
            
            csv_data.append({
                "ID": utt_id,
                "duration": 1.0, # Replace with actual duration using torchaudio.info
                "wav": str(audio_file.resolve()),
                "spk_id": spk_id
            })

    with open(output_csv, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "duration", "wav", "spk_id"])
        writer.writeheader()
        writer.writerows(csv_data)
        
    print(f"Generated annotation file: {output_csv} with {len(csv_data)} utterances.")

if __name__ == "__main__":
    generate_speechbrain_csv("data/processed", "data/processed/train.csv")
