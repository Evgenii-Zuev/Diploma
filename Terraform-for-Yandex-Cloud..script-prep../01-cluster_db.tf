resource "yandex_mdb_mysql_cluster" "my-mysql" {
  name                = "my-mysql"
  environment         = "PRODUCTION"
  network_id          = yandex_vpc_network.mynet.id
  version             = "5.7"
  security_group_ids  = [yandex_vpc_security_group.mysql-sg.id]
  deletion_protection = false

  resources {
    resource_preset_id = "c3-c2-m4"
    disk_type_id       = "network-hdd"
    disk_size          = 10
  }

  database {
    name = var.db
  }

  user {
    name     = var.user_name
    password = var.pass
    permission {
      database_name = var.db
      roles         = ["ALL"]
    }
  }
  host {
    zone      = var.zone
    subnet_id = yandex_vpc_subnet.mysubnet.id
  }
}

resource "yandex_vpc_security_group" "mysql-sg" {
  name       = "mysql-sg"
  network_id = yandex_vpc_network.mynet.id

  ingress {
    description    = "MySQL"
    port           = 3306
    protocol       = "TCP"
    v4_cidr_blocks = ["0.0.0.0/0"]
  }
}
