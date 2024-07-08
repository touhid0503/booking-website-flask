from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/admin/")
def admin():
    return "Hello Admin"


@app.route("/guest/<guest>")
def guest(guest):
    return "Hello %s" % guest


@app.route("/user/<name>")
def user(name):
    # return "Hello Admin"
    if name == "admin":
        return redirect(url_for("admin")) #redirect(url_for("function_name"))
    else:
        return redirect(url_for("guest", guest=name)) #redirect(url_for("function_name",variable_pass))


if __name__ == "__main__":
    app.run()
