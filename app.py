responses = []

from flask import Flask, render_template, request, redirect, flash
from surveys import satisfaction_survey, survey

app = Flask(__name__)

@app.route('/')
def starter():
  
  return render_template('base.html', title=satisfaction_survey.title, instructions=satisfaction_survey.instructions)

@app.route('/question/<num>')
def first(num):

  if (responses is None):
    return redirect("/")

  if (len(responses) == len(satisfaction_survey.questions)):
    return redirect("/complete")

  if (len(responses) != int(num)):
    flash('Wrong question')
    return redirect(f"/question/{len(responses)}")

  return render_template(f'question_0.html', question=satisfaction_survey.questions[int(num)].question, choices=satisfaction_survey.questions[int(num)].choices)


@app.route('/complete')
def comp():
  return render_template('complete.html') 


@app.route('/answer', methods=["POST"])
def ans():
  choice = request.form["choices"]
  responses.append(choice)
  if(len(responses) == len(satisfaction_survey.questions)):
    return redirect(f"/complete")
  else:
    return redirect(f"/question/{len(responses)}")
  