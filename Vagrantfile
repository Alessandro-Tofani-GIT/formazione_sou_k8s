# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
 
  config.vm.define "rocky" do |rocky|
    # Impostiamo il box di Rocky Linux 9
    rocky.vm.box = "rockylinux/9"
    
    # Configurazione della rete privata con IP statico
    rocky.vm.network "private_network", ip: "192.168.33.10"
    
    # Impostiamo la dimensione de disco con il plugin vagrant-disksize
    rocky.disksize.size = '50GB'
    
    # Configurazione del provider VirtualBox
    rocky.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"  # Imposta la RAM a 2GB
      vb.cpus = 2         # Imposta 2 CPU


    rocky.vm.provision "ansible" do |ansible|
      ansible.playbook= "playbook.yml"
      ansible.inventory_path= "inventory.ini"
    end
    end
  end
end



