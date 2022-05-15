resource "yandex_kubernetes_cluster" "<имя кластера>" {
 network_id = yandex_vpc_network.<имя сети>.id
 master {
   zonal {
     zone      = yandex_vpc_subnet.<имя подсети>.zone
     subnet_id = yandex_vpc_subnet.<имя подсети>.id
   }
 }
 service_account_id      = yandex_iam_service_account.<имя сервисного аккаунта>.id
 node_service_account_id = yandex_iam_service_account.<имя сервисного аккаунта>.id
   depends_on = [
     yandex_resourcemanager_folder_iam_binding.editor,
     yandex_resourcemanager_folder_iam_binding.images-puller
   ]
}

resource "yandex_vpc_network" "<имя сети>" { name = "<имя сети>" }

resource "yandex_vpc_subnet" "<имя подсети>" {
 v4_cidr_blocks = ["<диапазон адресов подсети>"]
 zone           = "<зона доступности>"
 network_id     = yandex_vpc_network.<имя сети>.id
}

resource "yandex_iam_service_account" "<имя сервисного аккаунта>" {
 name        = "<имя сервисного аккаунта>"
 description = "<описание сервисного аккаунта>"
}

resource "yandex_resourcemanager_folder_iam_binding" "editor" {
 # Сервисному аккаунту назначается роль "editor".
 folder_id = "<идентификатор каталога>"
 role      = "editor"
 members   = [
   "serviceAccount:${yandex_iam_service_account.<имя сервисного аккаунта>.id}"
 ]
}

resource "yandex_resourcemanager_folder_iam_binding" "images-puller" {
 # Сервисному аккаунту назначается роль "container-registry.images.puller".
 folder_id = "<идентификатор каталога>"
 role      = "container-registry.images.puller"
 members   = [
   "serviceAccount:${yandex_iam_service_account.<имя сервисного аккаунта>.id}"
 ]
}
