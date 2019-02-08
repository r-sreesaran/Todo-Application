from sqlalchemy import create_engine

# pip install SQLAlchemy

# class Todo(Base):
#     __tablename__ = 'Todo'
#     id = Column(Integer, primary_key=True)
#     text = Column(String(200))
#     complete = Column(Boolean)
#

sql_query = """
CREATE TABLE IF NOT EXISTS Todo (
  id INTEGER PRIMARY KEY,
  text TEXT,
  complete boolean
);
"""

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///todo.db')
engine.execute(sql_query)
