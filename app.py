from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from service import ToDoService
from flask import jsonify


app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"



@app.route("/create")
def create_items():
    
    params = {"text":"ironman","Description":"marvel"}
    return jsonify(ToDoService().create(params))
    
@app.route("/list")
def create_todo():
    return jsonify(ToDoService().getalldata())
    

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True,host="0.0.0.0")                     # run the flask app


