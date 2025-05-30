# Jenkins Pipeline - ENVIRONMENT Conditional Stages

Questa pipeline di Jenkins è configurata per eseguire operazioni condizionali basate sul valore del parametro `ENVIRONMENT`. La pipeline contiene due stage principali: **PRODUCTION** e **DEVELOPMENT**, che vengono eseguiti separatamente in base al valore di `ENVIRONMENT`.

## Descrizione della Pipeline

La pipeline è configurata come segue:

---

### Parametro `ENVIRONMENT`

Il parametro `ENVIRONMENT` definisce l'ambiente in cui verrà eseguita la pipeline. Le opzioni disponibili per questo parametro sono:
- `PRODUCTION`
- `DEVELOPMENT`

---

## Stages

La pipeline contiene due stage distinti che vengono eseguiti in base al valore del parametro `ENVIRONMENT`.

---

### Stage 'PRODUCTION'

- **Condizione**: Viene eseguito solo se `ENVIRONMENT == 'PRODUCTION'`.
- **Azione**: Quando questo stage è attivo, viene stampato il messaggio `Sono in PRODUCTION`.

---

### Stage 'DEVELOPMENT'

- **Condizione**: Viene eseguito solo se ENVIRONMENT == 'DEVELOPMENT'.
- **Azione**: Quando questo stage è attivo, viene stampato il messaggio Sono in DEVELOPMENT.

---

## Requisiti

- [Vagrant](https://www.vagrantup.com/downloads)
- [Ansible](https://www.ansible.com/download)

---

## Conclusioni

Questa pipeline è utile per separare l'esecuzione di diverse configurazioni in base all'ambiente di destinazione. Utilizzando il parametro ENVIRONMENT, è possibile eseguire la pipeline in modo flessibile e condizionale, adattandola facilmente a vari scenari di sviluppo e produzione.
