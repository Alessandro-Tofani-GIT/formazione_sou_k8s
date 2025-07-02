from flask import Flask 
app = Flask(__name__)

@app.route('/')
@app.route('/ita')
def hello():
	return "Ciao Mondo!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
