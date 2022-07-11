# [START functions_v2_basic]
variable "project_id" {
    default = "wellnecitydemo"
}

variable "region" {
    default = "US"
}

variable "name_suffix" {
    default = "demo"

}
provider "google" {
  project = "wellnecitydemo"
  region  = "US"
}
data "archive_file" "source" {
    type        = "zip"
    source_dir  = "./app"
    output_path = "/tmp/function.zip"
}

resource "google_storage_bucket" "bucket" {
  provider = google-beta
  project  = "wellnecitydemo"
  name     = "cloudfunctions2-function-bucket-bucket"  # Every bucket name must be globally unique
  location = "US"
  uniform_bucket_level_access = true
}

resource "google_storage_bucket_object" "object" {
  provider = google-beta
  name   = "Function from Terraform"
  bucket = google_storage_bucket.bucket.name
  source = data.archive_file.source.output_path
}

resource "google_cloudfunctions2_function" "terraform-test2" {
  provider = google-beta
  name = "test-function-terraform-test2"
  location = "us-central1"
  project = "wellnecitydemo"
  description = "a new function"

  build_config {
    runtime = "nodejs16"
    entry_point = "helloHttp"  # Set the entry point
    source {
      storage_source {
        bucket = google_storage_bucket.bucket.name
        object = google_storage_bucket_object.object.name
      }
    }
  }

  service_config {
    max_instance_count  = 1
    available_memory    = "256M"
    timeout_seconds     = 60
  }
}

