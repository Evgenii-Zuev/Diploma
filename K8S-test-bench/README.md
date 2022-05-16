### Создание тестового стенда для развертывания кластера k8s

- Готовим 5 виртуальных машин (1 - "установщик", 1 - "мастер" с etcd, и 3 - "воркера"). Это не совсем правильно, но для тестового кластера должно хватить.
- Настраиваем BIND на "установщике".
- Настраиваем подключение с "установщика" ко всем остальным по SSH

         ssh-keygen
         ssh-copy-id control1
         ssh-copy-id worker1
         ssh-copy-id worker2
         ssh-copy-id worker3
    
- Подготавливаем виртуалки для установки кластера при помощи ansible

         ---
         - name: Preparation
         -   hosts: k8s_cluster
         -     become: yes

  tasks:
  - name: Install packages
    yum:
      name:
        - net-tools
#        - mc
#        - vim
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

- Подготавливаем Kubespray
