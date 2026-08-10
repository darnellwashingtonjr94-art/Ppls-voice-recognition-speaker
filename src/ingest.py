import os
import argparse

def download_voxceleb(output_dir):
    """Downloads VoxCeleb dataset metadata and media."""
    print(f"Fetching VoxCeleb to {output_dir}...")
    # Insert actual wget/curl commands or API hooks for VoxCeleb

def download_common_voice(output_dir):
    """Downloads Mozilla Common Voice dataset."""
    print(f"Fetching Common Voice to {output_dir}...")
    # Insert HuggingFace datasets library load logic here

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--out_dir', type=str, default='data/raw')
    args = parser.parse_args()
    
    os.makedirs(args.out_dir, exist_ok=True)
    download_voxceleb(args.out_dir)
    download_common_voice(args.out_dir)
