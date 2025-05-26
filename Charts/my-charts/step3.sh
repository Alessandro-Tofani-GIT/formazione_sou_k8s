#!/bin/bash

API_SERVER="https://localhost:49375"
SA_NAME="sa-reader"
NAMESPACE="formazione-sou"
DEPLOYMENT_NAME="my-charts"
DEPLOYMENT_CHART_PATH="/Users/alessandro.tofani/Desktop/formazione_sou_k8s/Charts/$DEPLOYMENT_NAME"
FILE="deploy.yaml"


echo "Creo il DEPLOYMENT"
helm install $DEPLOYMENT_NAME $DEPLOYMENT_CHART_PATH -n $NAMESPACE

echo "Creo il service account nel $NAMESPACE"
kubectl create sa $SA_NAME -n $NAMESPACE

echo "Creo il token per il $SA_NAME nel $NAMESPACE" 
TOKEN_SA=$(kubectl create token "$SA_NAME" -n "$NAMESPACE")

sleep 5

echo 'Creo il ClusterRoleBinding'
kubectl create clusterrolebinding "${SA}-binding" --clusterrole=view --serviceaccount="$NAMESPACE:$SA_NAME"

echo "Faccio il curl per esportare il deployment tramite API Kubernetes..."
curl --insecure -H "Authorization: Bearer $TOKEN_SA" \
"$API_SERVER/apis/apps/v1/namespaces/$NAMESPACE/deployments/$DEPLOYMENT_NAME" -o $FILE

sleep 5


# READINESS_SEARCH=$(cat $FILE | grep readines)
# LIVENESS_SEARCH=$(cat $FILE| grep liveness)
# LIMITS_SEARCH=$(cat deploy.yaml | grep resources.limits )
# REQUESTS_SEARCH=$(cat deploy.yaml | grep resources.requests)

ERROR=0
    
# Check readinessProbe
jq -e ".spec.template.spec.containers[].readinessProbe" "$FILE" > /dev/null 2>&1 || { echo "❌ Mancante readinessProbe"; ERROR=1; }

# Controlla livenessProbe
jq -e '.spec.template.spec.containers[].livenessProbe' "$FILE" > /dev/null 2>&1 || { echo "❌ Mancante resources.livenessProbe"; ERROR=1; }


# Controlla resources.requests
jq -e '.spec.template.spec.containers[].resources.requests' "$FILE" > /dev/null 2>&1 || { echo "❌ Mancante resources.requests"; ERROR=1;  }

# Check resources.limits
jq -e ".spec.template.spec.containers[].resources.limits" "$FILE" > /dev/null 2>&1 || { echo "❌ Mancante resources.limits"; ERROR=1; }

if [ "$ERROR" -ne 0 ]; then
  echo "❌ Deployment NON valido: mancano uno o più attributi richiesti." >&2
  exit 1

else
  echo "✅ Deployment valido"
  exit 0
fi

