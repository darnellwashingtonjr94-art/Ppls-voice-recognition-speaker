variable "aws_region" {
  description = "The AWS region to deploy the GPU inference node"
  type        = string
  default     = "us-east-1"
}

variable "db_volume_size" {
  description = "Size of the attached volume for audio and SQLite DB (in GB)"
  type        = number
  default     = 500
}
