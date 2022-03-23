from flask import Flask

app = Flask(__name__)

@app.route('/')
def sayHi():
	return "Hi" 

# /welcome
# Returns “welcome”
@app.route('/welcome')
def show_welcome():
	return "Welcome"


# /welcome/home
# Returns “welcome home”
@app.route('/welcome/home')
def show_welcome_back():
	return "Welcome home"

# /welcome/back
# Return “welcome back”
@app.route('/welcome/back')
def show_welcome_home():
	return "Welcome back"