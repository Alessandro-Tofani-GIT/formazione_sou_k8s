# Jenkins CI/CD Pipeline per Applicazione Flask Dockerizzata

Questo repository contiene una pipeline di Jenkins per automatizzare il processo di build e deployment di un'applicazione Flask utilizzando Docker. La pipeline è progettata per gestire diverse branch e tag, automatizzando il processo di creazione dell'immagine Docker, tagging e push su Docker Hub.

## Indice

1. [Panoramica](#panoramica)
2. [Stadi della Pipeline](#stadi-della-pipeline)
3. [Variabili di Ambiente](#variabili-di-ambiente)
4. [Utilizzo](#utilizzo)
5. [Prerequisiti](#prerequisiti)

---

## Panoramica

Questa pipeline automatizza i seguenti passaggi:
- **Login Docker**: Eseguito utilizzando le credenziali salvate nel Jenkins.
- **Checkout del Repository Git**: Il repository viene clonato o aggiornato in base al branch o tag specificato.
- **Creazione e Tagging dell'Immagine Docker**: La pipeline costruisce un'immagine Docker utilizzando il `Dockerfile` e la tagga in base al branch o al tag Git.
- **Push dell'Immagine su Docker Hub**: L'immagine Docker viene inviata a Docker Hub per la distribuzione.

## Stadi della Pipeline

La pipeline è suddivisa in diverse fasi, ognuna con uno scopo specifico:

### 1. **Docker login**
   - Esegue il login su Docker Hub utilizzando le credenziali salvate nel sistema Jenkins.
   - Modifica i permessi del socket Docker per consentire l'accesso a tutti gli utenti.

### 2. **Check dell'Immagine**
   - Verifica quale tag utilizzare per l'immagine Docker in base al branch Git (`main`, `develop` o tag specifico).
   - Aggiunge il tag appropriato all'immagine (es. `latest`, `develop-<commitSHA>`, o un tag personalizzato).

### 3. **Pull del Repository Git**
   - Clona o aggiorna il repository Git in base al branch specificato.
   - In base al branch (`main`, `develop` o tag), esegue il pull delle ultime modifiche e costruisce l'immagine Docker.
   - Costruisce l'immagine Docker utilizzando il `Dockerfile`, la tagga e la invia su Docker Hub.

## Variabili di Ambiente

La pipeline fa uso delle seguenti variabili di ambiente:

- **DOCKER_NETWORK**: Nome della rete Docker.
- **DOCKER_CREDENTIALS**: ID delle credenziali di Docker salvate in Jenkins.
- **REPO_URL**: URL del repository Git da clonare.
- **REPO_DIR**: Nome della directory del repository.
- **IMAGE_TAG**: Tag dell'immagine Docker, determinato dinamicamente in base al branch o al tag Git.
- **BRANCH**: Parametro stringa che specifica branch.
- **TAG_IMAGE**: Tag Git

## Parametri della Pipeline

La pipeline accetta i seguenti parametri, che puoi configurare al momento dell'esecuzione:

### 1. **BRANCH**
   - Tipo: `String`
   - **Descrizione**: Specifica il branch Git da cui fare il pull e costruire l'immagine Docker. 

### 2. **TAG_IMAGE**
   - Tipo: `String`
   - **Descrizione**: Specifica un tag Git per effettuare il checkout di uno snapshot preciso del repository.   
  
## Utilizzo

1. **Configurazione delle credenziali Docker su Jenkins**:
   - Aggiungi le credenziali di Docker Hub come una credenziale tipo `usernamePassword` in Jenkins. Usa il campo `DOCKER_CREDENTIALS` per fare riferimento a questa credenziale nel pipeline.

2. **Configurazione del repository Git**:
   - Imposta il URL del repository Git nel campo `REPO_URL`.
   - La pipeline supporta i branch `main`, `develop` e i tag Git.

3. **Esecuzione della pipeline**:
   - La pipeline può essere eseguita automaticamente ad ogni push o tag nel repository Git.
   - Jenkins eseguirà i vari stadi in sequenza: login Docker, controllo del tag immagine, pull del repository, e creazione e push dell'immagine Docker.

## Prerequisiti

- **Jenkins**: Assicurati che Jenkins sia configurato correttamente con il plugin Docker e con il supporto per le pipeline.
- **Docker**: Docker deve essere installato sul nodo in cui Jenkins esegue la pipeline.
- **Git**: Git deve essere configurato per il clonaggio del repository.
- **Credenziali Docker**: Le credenziali per Docker Hub devono essere configurate in Jenkins.



