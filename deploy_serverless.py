import os
import sys
import subprocess
import boto3

def run_job_pipeline(source_audio_url, reference_image_path, output_key):
    """
    Executes the build pipeline within the container environment
    and pushes the resulting master artifact to object storage.
    """
    print(f"[*] Starting job for payload: {source_audio_url}")

    # Stage 1: Fetch source audio
    print("[*] Downloading input audio file...")
    subprocess.run(["curl", "-sSL", source_audio_url, "-o", "raw_vocal_take.wav"], check=True)

    # Stage 2: Run master pipeline script
    print("[*] Executing build pipeline...")
    result = subprocess.run(["bash", "build_pipeline.sh"], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"[!] Pipeline Execution Failed:\n{result.stderr}")
        sys.exit(1)

    print("[*] Build completed successfully.")

    # Stage 3: Push output to S3-compatible Cloud Storage / CDN
    s3_endpoint = os.getenv("S3_ENDPOINT_URL")
    bucket_name = os.getenv("STORAGE_BUCKET_NAME")
    
    if s3_endpoint and bucket_name:
        print("[*] Uploading artifact to object storage...")
        s3 = boto3.client("s3", endpoint_url=s3_endpoint)
        s3.upload_file("output/final_robot_rap_master.mp4", bucket_name, output_key)
        print(f"[*] Deployment artifact published to: {bucket_name}/{output_key}")
    else:
        print("[!] Storage credentials missing. Artifact stored locally at output/final_robot_rap_master.mp4")

if __name__ == "__main__":
    audio_url = os.getenv("SOURCE_AUDIO_URL", "https://example.com/input.wav")
    img_path = os.getenv("REF_IMAGE_PATH", "image.png")
    out_key = os.getenv("OUTPUT_KEY", "renders/robot_rap_master.mp4")

    run_job_pipeline(audio_url, img_path, out_key)
