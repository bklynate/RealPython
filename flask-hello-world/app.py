# imports the Flask class from the flask module
from flask import Flask 

# creates the application objects
app = Flask(__name__)

# uses decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# defines the view using a function, which returns a string
def hello_world():
	return "Hello, world"

# starts the development server using the run() method
if __name__ == "__main__":
	app.run()