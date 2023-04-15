from flask import Flask, render_template, request
from surveys import satisfaction_survey

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "very_secret"
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def welcome():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('survey_home.html', survey_title = title, instructions = instructions)

@app.route('/questions/<num>')
def show_form(num):
    num = int(num)
    question = satisfaction_survey.questions[num].question
    choices = satisfaction_survey.questions[num].choices
    num += 1
    return render_template('questionnaire.html', question = question, choice0 = choices[0], choice1 = choices[1])

@app.route('/questions/submit', methods=["POST"])
def submit_data():
    look_at_args = request.args["option"]
    responses.append(look_at_args)
    return 
    
