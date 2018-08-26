from flask import Flask
from flask import render_template

app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Works~!"
    return render_template('index.html', message=message)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
