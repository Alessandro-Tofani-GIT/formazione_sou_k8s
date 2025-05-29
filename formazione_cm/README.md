##Ansible Playbook: Installazione Docker e Registry Privato

Questo playbook Ansible automatizza l'installazione di Docker su un host Rocky Linux (o CentOS compatibile) e avvia un Docker registry privato senza autenticazione, esposto sulla porta 5000.

---
## 📌 Funzionalità

- Installa Docker CE e le sue dipendenze
- Configura il repository ufficiale Docker
- Abilita e avvia il servizio Docker
- Installa `pip` e i pacchetti Python necessari per l'uso dei moduli Docker in Ansible
- Avvia due container:
  - Un container di test basato sull'immagine ufficiale `docker`
  - Un container `registry:2` per ospitare un registry Docker privato

---

##Requisiti

Vagrant installato (per creare e gestire la VM target)
Ansible installato sulla macchina host (controllo)
Una VM  avviata tramite Vagrant (Rocky 9 in questo caso)
