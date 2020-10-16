# -*- coding: utf-8 -*-
import os

import requests
import requests_cache
from flask import Flask, jsonify, render_template, request

rc = requests_cache()


def create_app():
    app = Flask(__name__)

    config_type = os.getenv("CONFIG_TYPE", "config.DevelopmentConfig")
    app.config.from_object(config_type)

    rc.install_cache(
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
                "https://api.github.com/"
                f"search/users?q=location:{first}+language:{second}"
            )
            response_dict = requests.get(url).json()
            return jsonify(response_dict)
        return render_template("index.html")

    return app
