from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Counter custom
c = Counter('my_requests_total', 'Total requests')

@app.before_request
def before_request():
    c.inc()

@app.route('/')
def hello():
    return "Hello DevOps Tribe!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




