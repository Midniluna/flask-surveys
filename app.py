from flask import Flask, render_template, request, redirect, jsonify
from surveys import satisfaction_survey as survey

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "very_secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


responses = []

@app.route('/')
def welcome():
    return render_template('survey_home.html', survey = survey)

@app.route('/questions/<int:num>')
def show_form(num):
    question = survey.questions[num]
    num += 1
    return render_template('questionnaire.html', num = num, question = question)

@app.route('/submit', methods=["POST"])
def submit_data():
    args = request.form["option"]
    responses.append(args)
    return redirect(f'/questions/{len(responses)}')
    
