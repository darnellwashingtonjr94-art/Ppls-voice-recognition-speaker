from tasks import process_render_job

def trigger_batch_render(audio_url, image_path, destination_key):
    task = process_render_job.delay(audio_url, image_path, destination_key)
    print(f"Task enqueued. ID: {task.id}")
    return task.id

if __name__ == "__main__":
    trigger_batch_render(
        "https://example.com/audio.wav",
        "image.png",
        "renders/batch_01.mp4"
    )
