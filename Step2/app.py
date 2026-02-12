from flask import Flask
from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricsExporter
from prometheus_client import start_http_server

app = Flask(__name__)

# Start Prometheus server on a separate port
start_http_server(8000)  # Port visibile solo all'esterno se App Service lo permette

@app.route('/')
def hello():
    return "Hello DevOps Tribe!"

# Metriche custom
from prometheus_client import Counter
c = Counter('my_requests_total', 'Total requests')
@app.before_request
def before_request():
    c.inc()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




