provider "aws" {
  region = "us-east-1"
}

# S3 Storage Bucket for Media Artifacts
resource "aws_s3_bucket" "media_store" {
  bucket = "robot-rap-pipeline-storage"
}

# Redis Cluster for Celery Task Queue
resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "pipeline-redis"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"
  port                 = 6379
}

# ECS Cluster for Task Execution
resource "aws_ecs_cluster" "pipeline_cluster" {
  name = "robot-rap-cluster"
}
