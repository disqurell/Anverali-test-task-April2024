from flask import Flask
from api.handler import handler

app = Flask(__name__)
app.register_blueprint(handler, url_prefix="")
