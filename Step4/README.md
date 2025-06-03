# Jenkins Pipeline - Deploy di Helm Chart su Kubernetes

Questo progetto contiene un `Jenkinsfile` che automatizza il processo di **installazione di un'applicazione su Kubernetes** utilizzando **Helm**. La pipeline esegue tutte le operazioni necessarie, partendo dall’installazione degli strumenti fino al deploy vero e proprio.

---

## Obiettivo della Pipeline

Questa pipeline Jenkins è pensata per:

1. Installare automaticamente **Helm** e **kubectl** su un nodo Jenkins.
2. Clonare o aggiornare un **repository Git** contenente Helm charts.
3. Eseguire il **deploy di un'applicazione** su Kubernetes tramite Helm.

---

## Com’è strutturata la pipeline?

La pipeline è composta da diversi stage, ciascuno con uno scopo ben preciso.

### 1. `Installo Helm`

Scarica e installa **Helm 3**, lo strumento usato per gestire i pacchetti Kubernetes (chart).

---

### 2. `Installo kubectl`

Installa l’ultima versione stabile di `kubectl`, il client ufficiale per interagire con Kubernetes. Questo è utile per verificare la connessione e controllare lo stato del cluster.

---

### 3. `Pulling Charts`

Gestisce il codice che contiene i Helm chart:

- Se la cartella del repository **non esiste**, clona il repository da GitHub.
- Se la cartella **esiste già**, esegue un `git pull` per aggiornarla.
- Alla fine, esegue un **deploy dell'applicazione** su Kubernetes con `helm install`.

---

## Variabili di Ambiente

| Variabile             | Descrizione                                                        |
|----------------------|--------------------------------------------------------------------|
| `REPO_URL`           | URL del repository Git contenente i chart Helm                     |
| `REPO_DIR`           | Nome della directory locale dove clonare o aggiornare il repo      |
| `BRANCH`             | Branch Git da usare per scaricare i chart                          |
| `NAME_CHART`         | Nome da assegnare al rilascio Helm (es. nome dell'app)             |
| `CHART`              | Percorso del chart da installare (es. una sottocartella `Charts/`) |

---

## Requisiti

- Jenkins installato e configurato con un agente Linux.
- Accesso a un cluster Kubernetes (con `kubectl` configurato).
- Credenziali Docker configurate in Jenkins (`usernamePassword`).
- Il repository Git deve contenere un Helm chart valido.

---

## Esempio di utilizzo

Supponendo che il repository Git contenga un chart Helm chiamato `flask-app` nella cartella `my-charts`, questa pipeline:

1. Clona o aggiorna il repository.
2. Esegue `helm install flask-app my-charts` per installare l’applicazione nel cluster.

---


