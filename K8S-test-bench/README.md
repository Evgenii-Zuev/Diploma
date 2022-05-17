- [Безопасное хранение secrets в Kubernetes](https://habr.com/ru/company/southbridge/blog/658123/)

## Создание тестового стенда для развертывания кластера k8s

- Готовим 5 виртуальных машин (1 - "установщик", 1 - "мастер" с etcd, и 3 - "воркера"). Это не совсем правильно, но для тестового кластера должно хватить.
- Настраиваем BIND на "установщике" [K8S-test-bench (BIND settings)](https://github.com/Evgenii-Zuev/Diploma-preparation/tree/main/K8S-test-bench%20(BIND%20settings%20on%20the%20control%20machine))

- Настраиваем подключение с "установщика" ко всем остальным по SSH

         ssh-keygen
         ssh-copy-id control1.test-stand.local
         ssh-copy-id worker1.test-stand.local
         ssh-copy-id worker2.test-stand.local
         ssh-copy-id worker3.test-stand.local
         
- Проверка хостов для доступа ansible
1. **Hosts.txt**
```
[k8s_1st_master]
control1.test-stand.local ansible_host=192.168.1.101

[k8s_other_masters]

[k8s_controls:children]
k8s_1st_master
k8s_other_masters

[k8s_workers]
worker1.test-stand.local  ansible_host=192.168.1.102
worker2.test-stand.local  ansible_host=192.168.1.103
worker3.test-stand.local  ansible_host=192.168.1.104

[k8s_cluster:children]
k8s_controls
k8s_workers

```
2. **Playbook**
```
---
- name: Test playbook
  hosts: k8s_cluster
  become: yes

  tasks:
  - name: Ping my servers
    ping:
```
- Подготавливаем виртуалки для установки кластера при помощи ansible

         ---
         - name: Preparation
             hosts: k8s_cluster
               become: yes
               
               tasks:
               - name: Install packages
                 yum:
                   name:
                     - net-tools
                  #  - mc
                  #  - vim
                     - git
                     - bash-completion
                     - nfs-utils
                     - python3
                     - tar
                     - rsyslog
                  state: latest

              - name: Disable NetworkManager
                service:
                  name: NetworkManager
                  state: stopped
                  enabled: no

              - name: Enable rsyslog
                service:
                  name: rsyslog
                  state: started
                  enabled: yes

              - name: Enable network service
                service:
                  name: network
                  state: started
                  enabled: yes

              - name: Disable firewalld
                service:
                  name: firewalld
                  state: stopped
                  enabled: no

              - name: Check is swap enable
                shell: swapon
                register: swap_present
                changed_when: false
                ignore_errors: true

              - name: If swap is enabled - disable it
                shell: swapoff -a
                when: swap_present.stdout != ""

              - name: Disable SWAP in fstab
                replace:
                  path: /etc/fstab
                  regexp: '^([^#].*\s*swap\s*.*)$'
                  replace: '# \1'

              - name: Check Disable SELinux
                selinux:
                  state: disabled
                register: selinux_ret

              - name: Disable SELinux
                shell: setenforce 0
                when: selinux_ret.reboot_required

---
- Подготавливаем Kubespray (клонируем репозиторий. создаём inventory для ansible)
```
git clone https://github.com/kubernetes-sigs/kubespray
cd kubespray/inventory
cp sample cluster
cd cluster
```
- Мой **inventory.ini** в директории cluster 
```
[all]
control1.test-stand.local ansible_host=192.168.1.101
worker1.test-stand.local ansible_host=192.168.1.102
worker2.test-stand.local ansible_host=192.168.1.103
worker3.test-stand.local ansible_host=192.168.1.104

[kube-master]
control1.test-stand.local

[etcd]
control1.test-stand.local

[kube-node]
worker1.test-stand.local
worker2.test-stand.local
worker3.test-stand.local

[calico-rr]

[k8s-cluster:children]
kube-master
kube-node
calico-rr
```
- Параметры установки кластера K8S в файлах в директории group_vars

         1.Файл group_vars/k8s-cluster/k8s-cluster.yml

| Параметр   | Значение  |   Описание   |
|:--------|:------------|:-------------|
| kube_version1 |  v1.20.2 | версию кластера кубернетес |
| kube_network_plugin|calico|драйвер сети кластера|
|kube_service_addresses|10.233.0.0/18|диапазон адресов для сервисов кластера|
|kube_pods_subnet|10.233.64.0/18|диапазон адресов для подов кластера|
|kube_network_node_prefix|24|размер подсети подов на ноде кластера|
|kube_apiserver_port|6443|Порт API сервера кластера|
|kube_proxy_mode| ipvs|режим iptables не ставим|
|cluster_name|cluster.local|имя кластера (используется в качестве корневого домена во внутреннем DNS сервере)|
|enable_nodelocaldns|true|включаем кеширующие DNS сервера на каждой ноде кластера|
|nodelocaldns_ip|169.254.25.10|IP адрес кешируюшего DNS сервера на ноде|
|container_manager|containerd|определяем систему контейнеризации|
|k8s_image_pull_policy|IfNotPresent|политика загрузки образов системных контейнеров кластера|
|system_memory_reserved|512Mi|зарезервированная за Linux системой (приложениями) память|
|system_cpu_reserved|500m|зарезервированное за Linux системой (приложениями) время процессора|
|force_certificate_regeneration| true|Автоматический перевыпуск сертификатов для кубернетес control plane (без необходимости увеличения версии кластера)|
