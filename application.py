from flask import Flask
from flask import render_template

application = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@application.route("/")
def hello():
    message = "v0.1"
    return render_template('index.html', message=message)

@application.route("/privacy")
def privacy():
    message = "Works~!"
    return render_template('privacy.html', message=message)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    application.run()
