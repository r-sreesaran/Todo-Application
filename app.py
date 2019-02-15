from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from db_functions import add_todo_item, mark_complete, get_complete, get_incomplete, delete_item, move_back
from create_db import createtable

app = Flask(__name__)


@app.route('/')
def index(): 
    createtable()
    incomplete = get_incomplete()
    complete = get_complete()
    return render_template('index.html', incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST'])
def add():
    add_todo_item(text=request.form['todoitem'],priority=request.form['priority'])
    return redirect(url_for('index'))

@app.route('/undo/<id>')
def undo(id):
    move_back(id)
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    mark_complete(id)
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    delete_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
