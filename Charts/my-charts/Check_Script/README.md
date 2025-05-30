# Kubernetes Deployment Validation Script

Questo script Bash esegue un processo di validazione per un **Kubernetes Deployment** tramite `helm`, `kubectl`, e `curl`. Verifica che i parametri obbligatori come `readinessProbe`, `livenessProbe`, e `resources.requests` siano presenti nel manifest del deployment.

## Descrizione dello Script

Lo script ha il compito di:
1. **Installare un Deployment** utilizzando Helm.
2. **Creare un Service Account** nel namespace Kubernetes specificato.
3. **Generare un token per il Service Account**.
4. **Esportare il Deployment** tramite API Kubernetes usando `curl`.
5. **Controllare la presenza di attributi obbligatori** nel Deployment YAML (`readinessProbe`, `livenessProbe`, `resources.requests`, `resources.limits`).
6. **Restituire un errore** se uno o più attributi obbligatori sono mancanti.

### Parametri

- **API_SERVER**: URL del server API Kubernetes.
- **SA_NAME**: Nome del Service Account da creare.
- **NAMESPACE**: Namespace Kubernetes in cui creare il Service Account e il Deployment.
- **DEPLOYMENT_NAME**: Nome del Deployment da creare.
- **DEPLOYMENT_CHART_PATH**: Percorso del chart Helm per il Deployment.
- **FILE**: File in cui verrà esportato il Deployment YAML.

### Requisiti

- **Kubernetes CLI (`kubectl`)**: Per interagire con il cluster Kubernetes.
- **Helm**: Per installare il chart del Deployment.
- **jq**: Per analizzare e validare il file YAML del Deployment.
- **curl**: Per fare richieste HTTP alle API di Kubernetes.

## Installazione e Esecuzione

### 1. **Prepara l'ambiente**

Assicurati di avere i seguenti strumenti installati:

- [Helm](https://helm.sh/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [jq](https://stedolan.github.io/jq/)

### 2. **Configura lo Script**

Modifica lo script in base ai tuoi parametri:

- **API_SERVER**: Imposta l'URL del tuo server API Kubernetes.
- **SA_NAME**: Imposta il nome del Service Account che desideri creare.
- **NAMESPACE**: Sostituisci con il namespace Kubernetes che stai utilizzando.
- **DEPLOYMENT_NAME**: Imposta il nome del Deployment da creare.
- **DEPLOYMENT_CHART_PATH**: Specifica il percorso del chart Helm per il Deployment.

### 3. **Esegui lo Script**

Per eseguire lo script, apri il terminale e avvia il comando:

```bash
./deploy.sh

