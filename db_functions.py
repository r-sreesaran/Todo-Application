import sqlite3


def execute_query(sql_query):
    """
    function to execute sql commands
    :return: returns values if select command used
    """
    # print(sql_query)
    with sqlite3.connect("todo.db") as con:
        cur = con.cursor()
        result = cur.execute(sql_query)
        con.commit()
    return result


def add_todo_item(text,priority):
    """
    function to add todo text and its priority into the database
    :param text: text input by the user
    :return: None
    """
    sql_query = """insert into Todo(text1,priority,complete) VALUES ( '%s','%s',%s )""" % (text,priority, 0)
    execute_query(sql_query)


def mark_complete(id):
    """
    function to change the todo status as complete
    :param id: id of the todo item
    :return: None
    """
    sql_query = """UPDATE Todo set complete= %s where id= %s""" % (1, id)
    execute_query(sql_query)

def move_back(id):
    """
    function to undo the changes
    """
    sql_query = """ UPDATE Todo set complete= %s where id= %s """ % (0,id)
    execute_query(sql_query)

 
def get_complete():
    """
    function to get all complete todo items
    :return: items marked as done or 1 in the database
    """
    sql_query = """select * from Todo where complete = 1"""
    return execute_query(sql_query).fetchall()


def get_incomplete():
    """
    function to get all incomplete todo items
    :return: items marked as not done or 0 in the database
    """
    sql_query = """select * from Todo where complete = 0"""
    return execute_query(sql_query).fetchall()


def delete_item(id):
    """
    function to delete item 
    """
    sql_query = """ DELETE from Todo WHERE id= %s""" % (id)
    execute_query(sql_query)

def update_item(id,text,priority):
    """
    function to update item
    """
    sql_query = """ UPDATE Todo set text1 = '%s', priority = '%s' where id= %s""" % (text,priority,id)
    execute_query(sql_query) 