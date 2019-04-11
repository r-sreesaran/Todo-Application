import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        #self.create_user_table()
        self.create_to_do_table()
        self.conn = sqlite3.connect('userinformation.db')
        self.create_user_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          emailid VARCHAR(320) 
        ); 
        """

        self.conn.cursor().execute(query)
        self.conn.commit()
    
    def create_user_table(self):
        
        query = """
        CREATE TABLE IF NOT EXISTS "UserInformation" (
           emailid  VARCHAR(320) PRIMARY KEY,
           password VARCHAR(320) 
        );       
        """ 
        self.conn.cursor().execute(query)
        self.conn.commit()

class ToDoModel:
    
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        TABLENAME = "Todo"
        query = f'insert into {TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'
        
        self.conn.cursor().execute(query)
        self.conn.commit()
        return "sucess"

    def get_alldata(self):
        TABLENAME = "Todo"
        query = f'select * FROM {TABLENAME}'
        result = self.conn.cursor().execute(query)
        self.conn.commit()
        return result.fetchall()
       

   # Similarly add functions to select, delete and update todo

class User:

    def __init__(self):
        self.conn = sqlite3.connect('userinformation.db')

    def create(self,email,password):
         TABLENAME = "UserInformation"
         query = f'insert into {TABLENAME} ' \
                 f'(emailid, password) ' \
                 f'values ("{email}","{password}")'
         self.conn.cursor().execute(query)
         self.conn.commit()

