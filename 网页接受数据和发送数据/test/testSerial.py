from flask import Flask
from flask import render_template
from flask import request
import serial,json
from time import sleep

data = ''
app = Flask(__name__)
@app.route('/')
def hello_world():
	return render_template("index.html")

#新加的东西；
@app.route('/login')
def login():
	getData = request.args['data']
	if getData == 'o':
		#执行相应的操作，舵机或者灯亮，但是一定要把硬件弄的树莓派上；
		print('在这执行相关的操作')
		#给客户端返回数据，不用管数据是啥，但要有返回值；
	return json.dumps("ok")


@app.route('/ceshi')
def ceshi():
	serialcc = serial.Serial('COM5', 9600, timeout=0.5)
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
	return json.dumps(zuowei)


if __name__ == '__main__':
	app.run(port=8888)