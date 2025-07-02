# Jenkins Master-Slave Automation con Ansible, Vault e Vagrant

## Descrizione

Questo progetto automatizza la configurazione di un ambiente Jenkins master-slave utilizzando Ansible.  
La configurazione prevede due macchine virtuali (master e slave) create con Vagrant e VirtualBox.  
Le credenziali sensibili sono protette tramite **Ansible Vault**.  
I playbook sono organizzati in ruoli per una gestione modulare e riutilizzabile.

---

## Prerequisiti

- [Vagrant](https://www.vagrantup.com/) (>= 2.2)  
- [VirtualBox](https://www.virtualbox.org/)  
- [Ansible](https://www.ansible.com/) (>= 2.9)  
- Plugin Vagrant `vagrant-disksize` (per gestire la dimensione del disco)  
- File password di Vault (`~/.vault_pass.txt`) correttamente configurato  
  

---


- **Vagrantfile**: definisce le VM `rocky` (master) e `ubuntu` (slave) con rete privata e provisioning Ansible  
- **playbook.yml**: playbook principale che esegue i ruoli sui rispettivi host  
- **roles/**: ruoli Ansible per gestione master e slave  
- **Vault_file/vault.yml**: variabili protette da Ansible Vault (token, password, ecc.)  
- **jenkins_cookies.txt**: file cookie utilizzato per autenticazione Jenkins  
- **.vault_pass.txt**: file contenente la password per Ansible Vault   

---

## Configurazione Vagrant

Il file `Vagrantfile` definisce due VM:

- **rocky** (IP: 192.168.168.33): esegue Jenkins Master e crea agenti slave  
- **ubuntu** (IP: 192.168.168.32): esegue agenti slave e li sincronizza con il master  

Ogni VM ha:
- Provisioning automatico tramite Ansible con utilizzo di Vault per le variabili sensibili  




