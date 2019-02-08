from flask import Flask

app = Flask(__name__)
"""
__name__ is a built-in variable which evaluates to the name of the current module

When you write app = Flask(__name__) 
Think of it like - "using namespace std;" in C code
If you are using a single module, __name__ is always the correct value. If you however are using a package, 
it’s usually recommended to hardcode the name of your package there.
"""

"""
@app.route is a decorator
Simply put, a decorator is a wrapper around the function below it.
By definition, a decorator is a function that takes another function and extends the behavior of the 
latter function without explicitly modifying it.
"""


@app.route("/")
def hello_world():
    return "Hello World"


"""
If you do not want to use the decorator you can use the following code
"""

# app.add_url_rule("/", "hello", hello_world)
app.run(host="0.0.0.0", port=3200, debug=True)
