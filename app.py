
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/projects")
def projects():
    return render_template("projects.html.j2")

@app.route("/datasets")
def datasets():
    return render_template("datasets.html.j2")

@app.route("/models")
def models():
    return render_template("models.html.j2")

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5000)
