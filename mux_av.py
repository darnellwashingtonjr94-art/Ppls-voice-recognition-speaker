import subprocess
import os

def mux_audio_video(video_in, audio_in, final_out):
    """
    Merges the processed robotic audio track with the generated Veo video.
    """
    if not os.path.exists(video_in) or not os.path.exists(audio_in):
        raise FileNotFoundError("Missing required audio or video input files.")

    print(f"Muxing {video_in} and {audio_in}...")
    
    # FFmpeg command to combine streams and truncate to the shortest input
    command = [
        'ffmpeg', '-y',
        '-i', video_in,
        '-i', audio_in,
        '-c:v', 'copy',       # Preserve original video rendering
        '-c:a', 'aac',        # Standardize audio codec for web playback
        '-b:a', '256k',       # High bitrate to preserve vocoder fidelity
        '-map', '0:v:0',      # Take video from first input
        '-map', '1:a:0',      # Take audio from second input
        '-shortest',          # Sync termination
        final_out
    ]
    
    subprocess.run(command, check=True)
    print(f"Build successful. Final render compiled at: {final_out}")

if __name__ == "__main__":
    # Example execution paths
    mux_audio_video(
        video_in="output/robot_rap_scene_0.mp4", 
        audio_in="dlow_robot_rap.wav", 
        final_out="output/final_robot_rap_master.mp4"
    )
