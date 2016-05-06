from flask import Flask

import LED

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/scan', methods = ['POST'])
def scan():
	print("Scan!!!")
	LED.rainbow()
	return 'Scanned!!!'

@app.route('/prynt', methods = ['POST'])
def prynt():
	print("Prynt a picture!!")

	return 'Prynt a picture'


@app.route('/cash', methods = ['POST'])
def cash():
	print("Yeah baby $$ !!")

	return 'Yeaaah baby !!! $$$$'


@app.route('/new_account', methods = ['POST'])
def new_account():
	print("create new account")
	
	return 'Did create new account!!'

	
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
