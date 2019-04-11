import sqlite3
from models import ToDoModel,Schema,User

class ToDoService:
    def __init__(self):
        Schema()
        self.model = ToDoModel()
        
    def create(self, params):
        return self.model.create(params["text"], params["Description"])


    def getalldata(self):   
        return self.model.get_alldata()


class UserService:
      def __init__(self):
          Schema()
          self.user = User()

      def create(self,params):
          self.user.create(params['emailid'],params['password'])
       
       