from flask import Flask, render_template, flash, url_for

app = Flask(__name__)
# name will be changed later, configs will be added later

@app.route("/")
def IntroductionPage():
    return render_template('Introduction.html')

# change links to the route, demo shown below,
# note: Theory page not modified, only routing is shown here, so all other pages will follow this format
# add app.route to each page that needs one, use url_for() to redirect do we dont face problems if we move files anytime.

@app.route("/Theory")
def TheoryPage():
    return render_template('Theory.html')

@app.route("/Objective")
def ObjectivePage():
    return render_template('Objective.html')

@app.route("/Experiment")
def ExperimentPage():
    return render_template('Experiment.html')

@app.route("/Manual")
def ManualPage():
    return render_template('Manual.html')

@app.route("/Quizzes")
def QuizzesPage():
    return render_template('Quizzes.html')

@app.route("/Procedure")
def ProcedurePage():
    return render_template('Procedure.html')

@app.route("/Refrences")
def RefrencesPage():
    return render_template('Refrences.html')

@app.route("/Feedback")
def FeedbackPage():
    return render_template('Feedback.html')


if __name__ == '__main__':
    app.run(debug=True)
