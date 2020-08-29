from flask import Flask
from flask import render_template
import serial,json
from time import sleep

data = ''
app = Flask(__name__)
i = 0
@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/ceshi')
def ceshi():
	#serialcc = serial.Serial('COM3', 115200, timeout=0.5)

	ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
	#选用串口或者usb
	while True:
		data = serialcc.read_all()
		data=data.decode('UTF-8').replace('\t','').replace('\n','')
		if data == '':
			continue
		else:
			#if(len(data) == 22):
			zuowei=data.split('+')
			break
	print(len(zuowei))
	print(zuowei)
	return json.dumps(zuowei)


if __name__ == '__main__':
	app.run(port=8888)
