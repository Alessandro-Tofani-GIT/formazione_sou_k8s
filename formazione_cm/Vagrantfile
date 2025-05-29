# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
 
  config.vm.define "rocky" do |rocky|
    # Impostiamo il box di Rocky Linux 9
    rocky.vm.box = "rockylinux/9"
    
    # Configurazione della rete privata con IP statico
    rocky.vm.network "public_network", ip: "192.168.0.2"
    # Impostiamo la dimensione del disco con il plugin vagrant-disksize
    rocky.disksize.size = '50GB'
    
    # Configurazione del provider VirtualBox
    rocky.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"  # Imposta la RAM a 4GB
      vb.cpus = 4         # Imposta 4 CPU
    end

    # Provisioning con Ansible
    rocky.vm.provision "ansible" do |ansible|
      ansible.playbook = "container-playbook.yml"
      #ansible.inventory_path = "inventory.ini"  # Puoi scommentare questa riga se hai un file di inventario Ansible
    end

    # Provisioning con Shell per installare kubectl
    # rocky.vm.provision "shell", inline: <<-SHELL
    #   curl -LO https://dl.k8s.io/release/v1.24.0/bin/linux/amd64/kubectl
    #   sudo install kubectl /usr/local/bin/
    # SHELL
  end
end




