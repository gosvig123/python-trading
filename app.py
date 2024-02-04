#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
from flask import Flask
import os
from pandas import DataFrame

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return app.send_static_file("index.html")

    return app


create_app().run(host="0.0.0.0", port=9000)