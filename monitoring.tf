# CloudWatch Log Group for Celery Workers
resource "aws_cloudwatch_log_group" "pipeline_logs" {
  name              = "/ecs/robot-rap-pipeline" 
  retention_in_days = 14 # Specifies the number of days you want to retain log events
  
  tags = {
    Environment = "production"
    Application = "AI-Video-Pipeline"
  }
}

# Update the existing ECS Cluster to enable Container Insights with Prometheus support
resource "aws_ecs_cluster" "pipeline_cluster" {
  name = "robot-rap-cluster"

  setting {
    name  = "containerInsights"
    value = "enhanced" 
  }
}
