 variable "zone" {
  default = "ru-central1-a"
}

variable "yandex-token" {
  default = "<yandex token here>"
}

variable "yandex-cloud-id" {
  default = "<yandex cloud id here>"
}

variable "yandex-folder-id" {
  default = "<yandex folder id here>"
}

variable "instance_root_disk" {
  default = "8"
}

variable "instance_additional_disk" {
  default = "5"
}

# base name
variable "db" {
  default = "the_beatles"
}

# name of the user to access the database 
variable "user_name" {
  default = "<user name>"
}

# password to access the database
variable "pass" {
  default = "<password>"
}
