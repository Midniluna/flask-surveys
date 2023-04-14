from flask import Flask, render_template, request
import surveys

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "very_secret"
debug = DebugToolbarExtension(app)

