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

@app.route("/Experiment")
def ExperimentPage():
    return render_template('Experiment.html')

if __name__ == '__main__':
    app.run(debug=True)
