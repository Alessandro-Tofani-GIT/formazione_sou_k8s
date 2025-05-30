# Flask Application with Docker

Questo repository contiene un'applicazione web sviluppata con **Flask**, un micro-framework Python, e containerizzata utilizzando **Docker**. L'applicazione espone un semplice endpoint che restituisce il messaggio "Hello DevOps Tribe!" quando viene visitato l'endpoint principale.

## Panoramica

L'applicazione è un servizio web di base costruito con **Flask**, configurato per essere eseguito all'interno di un container Docker. L'uso di Docker garantisce che l'applicazione possa essere eseguita in modo coerente in qualsiasi ambiente, rendendola facilmente distribuibile. Il Dockerfile incluso nel repository crea un'immagine personalizzata per eseguire l'applicazione Flask.

## Componente Software

L'applicazione è composta da un singolo script Python (`app.py`) che implementa un'applicazione Flask. Quando l'utente visita il percorso principale (`/`), il server restituisce un messaggio di benvenuto:

---

## Dockerfile

Il Dockerfile contiene le istruzioni necessarie per costruire un'immagine Docker per il progetto. Questo file configura l'ambiente per l'esecuzione dell'applicazione Flask, installando le dipendenze Python e configurando il contenitore per eseguire l'applicazione.

## Descrizione di `app.py`

Il file `app.py` contiene il codice sorgente dell'applicazione Flask. Si tratta di una semplice applicazione web che espone un endpoint di base, `/`, che restituisce una stringa di testo.

## Descrizione di requirment.txt

Elenca le dipendenze necessarie per l'applicazione Flask.

--- 

## Prerequisiti

Per eseguire questo progetto, assicurati di avere i seguenti strumenti installati sulla tua macchina:

1. **[Docker](https://www.docker.com/get-started)**: Docker deve essere installato per costruire e eseguire i container. Segui la guida ufficiale per l'installazione di Docker.
2. **[Python](https://www.python.org/)**: Python deve essere installato se desideri eseguire l'applicazione al di fuori del container. Puoi scaricare l'ultima versione di Python dal sito ufficiale.
3. **[Git](https://git-scm.com/)**: Git è necessario per clonare il repository e gestire il codice sorgente. Puoi installarlo seguendo la guida ufficiale di Git.

