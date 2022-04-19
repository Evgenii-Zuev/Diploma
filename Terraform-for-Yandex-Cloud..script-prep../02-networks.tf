resource "yandex_vpc_network" "mynet" {
  name        = "mynet"
  description = "My Network"

  labels = {
    tester      = "Evgenii Zuev"
    environment = "Project Setup"
  }
}

resource "yandex_vpc_subnet" "mysubnet" {
  name           = "mysubnet"
  description    = "My Subnet"
  zone           = var.zone
  network_id     = yandex_vpc_network.mynet.id
  v4_cidr_blocks = ["10.5.0.0/24"]

  labels = {
    tester      = "Evgenii Zuev"
    environment = "Project Setup"
  }
}
