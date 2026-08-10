provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "voice_inference_node" {
  ami           = "ami-0c55b159cbfafe1f0" # Deep Learning AMI
  instance_type = "g4dn.xlarge"           # NVIDIA T4 GPU

  tags = {
    Name        = "Speaker-Recognition-Engine"
    Environment = "Production"
  }

  user_data = <<-EOF
              #!/bin/bash
              docker run -d -p 8000:8000 \
                -v /mnt/data:/app/data \
                --gpus all \
                ppls-voice-engine:latest
              EOF
}
