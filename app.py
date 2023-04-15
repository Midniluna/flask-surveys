from flask import Flask, render_template, request, redirect, flash
from surveys import satisfaction_survey as survey

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "very_secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


responses = []

@app.route('/')
def welcome():
    """Shows home page"""
    return render_template('survey_home.html', survey = survey)

@app.route('/questions/<int:num>')
def show_form(num):
    """Take users through questions and redirecting if number of responses does not correlate to question number"""
    if not len(responses) == num:
        flash("Invalid action", "error")
        return redirect(f'/questions/{len(responses)}')
    if num == len(survey.questions):
        return redirect('/completed')
    
    num = len(responses)
    question = survey.questions[num]
    return render_template('questionnaire.html', num = num, question = question)

@app.route('/submit', methods=["POST"])
def submit_data():
    """appends data to responses list"""
    args = request.form["option"]
    responses.append(args)
    return redirect(f'/questions/{len(responses)}')
    
@app.route('/completed')
def completed():
    """Check if user has completed the survey. if so, user is thanked and will not be able to re-complete it. If not, user is redirected to survey"""

    if not len(responses) == len(survey.questions):
        flash ("Please finish the survey", "error")
        return redirect(f'/questions/{len(responses)}')
    return render_template('/completed.html')