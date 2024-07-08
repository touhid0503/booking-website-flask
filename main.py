from flask import Flask

app = Flask(__name__)


# @app.route("/")
# @app.route("/<name>")
@app.route("/<int:id>/")

# def hello_world(name):
#     return "Welcome back %s" % name


def hello_world(id):
    return "The number is %d" % id


# app.add_url_rule("/h",'hello',hello_world)
if __name__ == "__main__":
    app.run()


# This is a simple web application built using the Flask framework in Python. Here's a brief explanation of each part of the code:

# 1. **Importing Flask**: The code starts by importing the `Flask` class from the `flask` module.

#    ```python
#    from flask import Flask
#    ```

# 2. **Creating a Flask App**: An instance of the `Flask` class is created and assigned to the `app` variable. This instance will be the web application.

#    ```python
#    app = Flask(__name__)
#    ```

# 3. **Defining a Route**: The `@app.route("/")` decorator is used to define a route for the root URL ("/"). When a user visits this URL, the function `hello_world` is called.

#    ```python
#    @app.route("/")
#    def hello_world():
#        return "Welcome 2"
#    ```

# 4. **Running the App**: The `if __name__ == "__main__":` block ensures that the web server runs only if the script is executed directly (not imported as a module). `app.run()` starts the Flask development server.

#    ```python
#    if __name__ == "__main__":
#        app.run()
#    ```

# ### Summary

# - **Flask Application**: This is a minimal Flask application.
# - **Route Definition**: It defines one route (`/`) that returns the string "Welcome 2" when accessed.
# - **Starting the Server**: The server starts when the script is run directly.
