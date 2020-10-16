# -*- coding: utf-8 -*-
import requests
import requests_cache
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

requests_cache.install_cache(
    "github_cache",
    backend="sqlite",
    expire_after=180,
)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        first = request.form.get("first")
        second = request.form.get("second")
        url = (
            f"https://ai.github.com/search/users?q"
            f"=location:{first}+language{second}"
        )
        response_dict = requests.get(url).json()
        return jsonify(response_dict)
    return render_template("index.html")
