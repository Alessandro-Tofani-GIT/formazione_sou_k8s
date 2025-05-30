# 📘 Ansible Playbook1: Gestione Utenti e Gruppi

## 🔍 Descrizione

Questo playbook Ansible automatizza la gestione degli utenti su un sistema Linux, eseguendo le seguenti operazioni:

- Verifica l'esistenza del gruppo `develop` e lo crea se necessario.
- Crea una lista di utenti specificati e li assegna al gruppo `develop`, configurando shell e home directory personalizzate.

## 🧩 Struttura del Playbook

Il playbook è suddiviso in due sezioni principali:

1. **Creazione del gruppo**  
   Utilizza il modulo `ansible.builtin.group` per assicurarsi che il gruppo `develop` esista.

2. **Creazione degli utenti**  
   Usa il modulo `ansible.builtin.user` per creare ciascun utente con i parametri specificati (nome, shell, gruppo, home directory).

## 🧰 Requisiti

- **Ansible**: Versione 2.5 o superiore.
- **Vagrant**: Per la gestione e l'orchestrazione di macchine virtuali di test.
- **Sistema di destinazione**: Linux (es. Ubuntu, CentOS).

## 🔁 Gestione con Dizionari e Loop

Il playbook sfrutta i dizionari per definire le proprietà degli utenti e i loop per iterare su di essi:

- **Dizionari**: Ogni utente è rappresentato come un dizionario che specifica il nome utente (`user`), lo stato desiderato (`state`), il gruppo di appartenenza (`groups`), la shell di login (`shell`) e la directory home (`home`). 
- **Loop**: Il modulo `loop` è utilizzato per iterare sulla lista `list-user`, creando gli utenti e assegnandoli al gruppo `develop`. Questo approccio consente di gestire facilmente un numero variabile di utenti senza duplicare il codice.

## 🚀 Esecuzione

Per eseguire il playbook:

```bash
ansible-playbook nome_playbook.yaml

---

# 📘 Ansible Playbook: Gestione Pacchetti Software

## 🔍 Descrizione

Questo playbook Ansible automatizza l'installazione e la rimozione di pacchetti software su host remoti. Utilizza una lista definita di pacchetti con il relativo stato desiderato (`present` per installare, `absent` per rimuovere) per eseguire le operazioni in modo dinamico.

## 🧩 Struttura del Playbook

- Il playbook è eseguito su tutti gli host definiti nell'inventario.
- Viene elevato il privilegio a root tramite `become: yes`.
- Definisce una variabile `lista` contenente dizionari, ciascuno rappresentante un pacchetto con il nome e lo stato richiesto.
- Il task principale usa il modulo `ansible.builtin.package` per gestire i pacchetti in base allo stato definito, iterando su ciascun elemento della lista tramite `loop`.

## 🧰 Requisiti

- **Vagrant**
- **Ansible**
- **Sistema di destinazione**: Linux con un gestore pacchetti supportato da Ansible (`apt`, `yum`, `dnf`, etc.).

## 🔁 Gestione con Dizionari e Loop

Il playbook utilizza:

- **Dizionari**: Ogni pacchetto è rappresentato da un dizionario con due chiavi: `name` (nome del pacchetto) e `state` (stato desiderato, ad esempio `present` o `absent`).
- **Loop**: Il modulo `loop` itera sulla lista `lista` per applicare la gestione dei pacchetti in modo dinamico e scalabile.

Questa struttura consente di aggiungere, rimuovere o modificare pacchetti semplicemente aggiornando la lista senza modificare il codice del task.

## 🚀 Esecuzione

Per eseguire il playbook:

```bash
ansible-playbook nome_playbook.yaml

