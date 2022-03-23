# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
	a1 = request.args.get("a", type=int)
	b1 = request.args.get("b", type=int)
	return str(add(a1,b1))

@app.route('/sub')
def sub_route():
	a1 = request.args.get("a", type=int)
	b1 = request.args.get("b", type=int)
	return str(sub(a1, b1))

@app.route('/mult')
def mult_route():
	a1 = request.args.get("a", type=int)
	b1 = request.args.get("b", type=int)
	return str(mult(a1, b1))

@app.route('/div')
def div_route():
	a1 = request.args.get("a", type=int)
	b1 = request.args.get("b", type=int)
	return str(div(a1, b1))

@app.route('/math/<operation>')
def operation_route(operation):
	a1 = request.args.get("a", type=int)
	b1 = request.args.get("b", type=int)
	operators ={
		"add": add,
		"sub": sub,
		"mult": mult,
		"div": div
	}
	result = operators[operation](a1,b1)
	return str(result)