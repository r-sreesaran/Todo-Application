from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from service import ToDoService, UserService
from flask import jsonify



app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"


@app.route("/login")
def login():
     pass

@app.route("/createUser",methods=["POST"])
def create_user():
     UserService().create(request.get_json()) 
     return 'usercreated'

@app.route("/deleteuser")
def delete_user():
    pass

    

@app.route("/create")
def create_items():
    
    params = {"text":"ironman","Description":"marvel"}
    return jsonify(ToDoService().create(params))
    
@app.route("/list")
def create_todo():
    return jsonify(ToDoService().getalldata())
    

if __name__ == "__main__":        
    app.run(debug=True,host="0.0.0.0")                     


