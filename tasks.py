import os
import logging
import subprocess
from celery import Celery
from prometheus_client import Counter, Histogram, start_http_server

# Initialize structured logging
logger = logging.getLogger("PipelineWorker")
logger.setLevel(logging.INFO)

# Prometheus Metrics Definitions
# CloudWatch Container Insights automates the discovery and collection of these metrics
RENDER_COUNT = Counter('job_render_total', 'Total number of video renders processed')
RENDER_FAILURES = Counter('job_render_failures', 'Total number of failed render jobs')
RENDER_DURATION = Histogram('job_render_duration_seconds', 'Time spent rendering the final AV payload')

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
app = Celery("pipeline_tasks", broker=redis_url, backend=redis_url)

# Start Prometheus metrics server on port 8000 for CloudWatch to scrape
start_http_server(8000)

@app.task(bind=True, max_retries=3)
def process_render_job(self, source_audio_url, ref_image_path, output_key):
    """
    Executes render job asynchronously with error tracking and telemetry.
    """
    RENDER_COUNT.inc()
    logger.info(f"Initiating render job for target: {output_key}")
    
    try:
        os.environ["SOURCE_AUDIO_URL"] = source_audio_url
        os.environ["REF_IMAGE_PATH"] = ref_image_path
        os.environ["OUTPUT_KEY"] = output_key
        
        with RENDER_DURATION.time():
            result = subprocess.run(
                ["bash", "build_pipeline.sh"], 
                capture_output=True, 
                text=True, 
                check=True
            )
            
        logger.info(f"Job completed successfully. Payload delivered to {output_key}")
        return {"status": "SUCCESS", "output_key": output_key}
        
    except subprocess.CalledProcessError as err:
        RENDER_FAILURES.inc()
        logger.error(f"Render job failed with exit code {err.returncode}. Standard Error: {err.stderr}")
        raise self.retry(exc=err, countdown=15)
