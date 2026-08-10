import os
from infer_rvc_python import BaseLoader

def generate_dlow_vocals(input_audio_path, output_audio_path):
    """
    Runs fast inference using a pre-trained RVC model.
    """
    # Initialize the base class
    # Set only_cpu=False to utilize GPU acceleration if available
    converter = BaseLoader(only_cpu=False, hubert_path=None, rmvpe_path=None)

    # Define the tag and load the BossMan Dlow model weights
    converter.apply_conf(
        tag="dlow_bounce",
        file_model="dlow_v2.pth", 
        pitch_algo="rmvpe+",
        pitch_lvl=0, # Adjust pitch if the source audio needs transposition
        file_index="dlow_v2.index",
        index_influence=0.66,
        respiration_median_filtering=3,
        envelope_ratio=0.25,
        consonant_breath_protection=0.33
    )

    print(f"Executing RVC inference on {input_audio_path}...")
    
    # Perform inference
    # Overwrite is set to False to prevent accidental data loss
    result = converter(
        input_audio_path,
        "dlow_bounce",
        overwrite=False,
        parallel_workers=4 
    )
    
    # Unload models from memory to free up VRAM for the video generation step
    converter.unload_models()
    print(f"Vocal generation complete. Output saved to: {result}")
    
    return result

if __name__ == "__main__":
    # Example execution
    source_acapella = "raw_vocal_take.wav"
    generate_dlow_vocals(source_acapella, "dlow_rvc_output.wav")
