import os
import subprocess
from celery import Celery

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
app = Celery("pipeline_tasks", broker=redis_url, backend=redis_url)

@app.task(bind=True, max_retries=3)
def process_render_job(self, source_audio_url, ref_image_path, output_key):
    """
    Executes render job asynchronously from queue payload.
    """
    try:
        os.environ["SOURCE_AUDIO_URL"] = source_audio_url
        os.environ["REF_IMAGE_PATH"] = ref_image_path
        os.environ["OUTPUT_KEY"] = output_key
        
        result = subprocess.run(["bash", "build_pipeline.sh"], capture_output=True, text=True, check=True)
        return {"status": "SUCCESS", "output_key": output_key}
    except subprocess.CalledProcessError as err:
        raise self.retry(exc=err, countdown=15)
