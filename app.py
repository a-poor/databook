
import json
import sqlite3
from pathlib import Path

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/projects")
def projects():
    # return render_template("projects.html.j2")
    return redirect("/")

@app.route("/datasets")
def datasets():
    return render_template("datasets.html.j2")

@app.route("/new-dataset")
def new_dataset():
    return render_template("new-dataset.html.j2")

@app.route("/datasets/<datasetname>")
def a_dataset(datasetname):
    dataset = {
        "name": datasetname,
        "description": ["the dataset's","description."],
        "cols": [
            {"name":"name","type":"string","desc":"The name of the person who is in this row of this very real table."},
            {"name":"age","type":"int8","desc":""},
            {"name":"is_french","type":"bool","desc":"But wait, is this person French? or not? If they are, this will be set to `true`."},
        ]
    }
    return render_template("adataset.html.j2",dataset=dataset)


if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5000)
