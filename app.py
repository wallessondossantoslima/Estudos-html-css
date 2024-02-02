from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "200"


@app.route("/header")
def header():
    return render_template("header/header.html")


@app.route("/mouseevent")
def mouseevent():
    return render_template("mouseevent/mouseevent.html")


@app.route("/ascii")
def ascii():
    return render_template("ascii/ascii.html")


@app.route("/icon")
def icon():
    return render_template("icon/icon.html")


if __name__ == "__main__":
    app.run(debug=True)
