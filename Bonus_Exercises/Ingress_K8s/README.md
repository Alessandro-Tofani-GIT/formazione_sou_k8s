#  Kubernetes Multi-Service Ingress Demo

Questo progetto Kubernetes implementa due microservizi, ciascuno esposto tramite un `Service` e accessibile tramite un unico Ingress controller sotto host comune `demo.local`, ma con due percorsi differenti:

-  `/ita` → Servizio `ita-service`
-  `/eng` → Servizio `eng-service`

##  Struttura delle risorse

| Tipo        | Nome               | Descrizione                                 |
|-------------|--------------------|---------------------------------------------|
| Deployment  | `ita-deployment`   | App `Ciao Mondo`, esposta sulla porta 5000      |
| Deployment  | `eng-deployment`   | App `Hello World`, esposta sulla porta 5000       |
| Service     | `ita-service`      | Service TCP  per `italia-deploy`            |
| Service     | `eng-service`      | Service TCP per `uk-deploy`                 |
| Ingress     | `ingress-formazionesou` | Ingress NGINX per indirizzare su path `/ita` e `/eng` |

---

##  Deployment

### 1. Assicurati di avere un Ingress Controller NGINX

> Assicurati di avere un Ingress Controller **NGINX** già installato, preferibilmente con tipo `LoadBalancer` su Docker Desktop.

Installa Ingress Controller NGINX:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
```

### 2. Modifica il file `/etc/hosts`

Aggiungi la seguente riga all'interno del file per risolvere demo.local localmente:

```bash
127.0.0.1 demo.local
```

### 3. Applica le risorse:

```bash
kubectl apply -f manifest.yml
```

### 4. Verifica sulle risorse

- Verifica dei pod:
```bash 
kubectl get pods
```

- Verifica dei service:
```bash
kubectl get svc
```

- Verifica dei Ingress:
```bash 
kubectl get ingress
```

---

## Build delle immagini Docker

Prima di eseguire il deployment su Kubernetes, è necessario creare le immagini Docker per i due servizi.

### Costruisci le immagini

`Ciao Mondo`:

```bash 
cd Images/Itas_Image
#Nome immagine a vostra discrezione comportando di conseguenza la modifica all'interno del manifest col nome da voi scelto
docker build -t italia:1.1 .
```

`Hello World`:

```bash 
cd Images/Itas_Image
#Nome immagine a vostra discrezione comportando di conseguenza la modifica all'interno del manifest col nome da voi scelto
docker build -t inglese:1.1 .
```

### Tips

- Se usi Docker Desktop, le immagini locali sono già accessibili.
- Se usi Kind, devi importarle manualmente:

```bash
kind load docker-image italia:1.1
kind load docker-image inglese:1.1
```
