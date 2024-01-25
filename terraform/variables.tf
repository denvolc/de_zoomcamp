variable "credentials" {
  description = "My Credentials"
  default     = "./keys/terraform_service.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project"
  default     = "spry-abacus-411519"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "europe-central2"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "europe-central2"
}

variable "bq_dataset_name" {
  description = "NY Dataset"
  #Update the below to what you want your dataset to be called
  default     = "ny_gr_taxi_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "ny_gr_taxi_data_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
