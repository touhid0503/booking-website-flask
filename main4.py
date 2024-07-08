from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/welcome/<user>")
def m(user):
    return render_template("index.html", name=user) #render_template


if __name__ == "__main__":
    app.run()
