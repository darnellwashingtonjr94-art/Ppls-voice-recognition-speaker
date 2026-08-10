import os
import time
from google import genai
from google.genai import types

def generate_robot_video(prompt_text, reference_image_path):
    """
    Calls the Google Veo API to generate a video using a text prompt and reference image.
    """
    # Ensure your API key is exported in your environment variables:
    # export GOOGLE_GEMINI_API_KEY="your_key_here"
    api_key = os.environ.get("GOOGLE_GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Error: GOOGLE_GEMINI_API_KEY environment variable not set")
    
    client = genai.Client(api_key=api_key)
    
    # Define the Veo model ID
    VEO_MODEL_ID = "veo-3.1"
    
    # Encode the first frame (the robot reference image)
    print(f"Encoding reference image: {reference_image_path}...")
    first_image = types.Image.from_file(location=reference_image_path)
    
    print("Submitting prompt to Veo API...")
    operation = client.models.generate_videos(
        model=VEO_MODEL_ID,
        prompt=prompt_text,
        config=types.GenerateVideosConfig(
            image=first_image,
            aspect_ratio="16:9", # Landscape orientation
            resolution="1080p",  # High-throughput resolution
            duration_seconds=8,  # Standard duration for Veo 3.1
            person_generation="allow_adult" # Configuration flag for human/character rendering
        ),
    )
    
    # Polling loop to wait for video generation completion
    print("Waiting for rendering pipeline to complete...")
    while not operation.done:
        time.sleep(20)
        print("Still rendering...")
        
    # Create output directory
    os.makedirs('./output', exist_ok=True)
        
    # Download and save the generated video(s)
    for n, generated_video in enumerate(operation.result.generated_videos):
        output_path = f'./output/robot_rap_scene_{n}.mp4'
        client.files.download(file=generated_video.video)
        generated_video.video.save(output_path)
        print(f"Video chunk {n} saved to {output_path}")

if __name__ == "__main__":
    # The prompt engineered for the specific visual bounce
    visual_prompt = (
        "The mechanical jaw moves rhythmically in precise lip-sync with fast rap cadence. "
        "Visible internal gears and cogwheels rotate in the cheek and jaw joints. "
        "Glowing holographic blue and orange soundwave symbols pulse outward from its mouth "
        "in time with the 808 bass beats. Studio lighting, sleek 3D render, "
        "photorealistic metallic reflections, dynamic motion blur, 4k resolution."
    )
    
    generate_robot_video(visual_prompt, "image.png")
