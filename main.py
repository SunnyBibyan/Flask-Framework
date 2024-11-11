from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this flask app Sunny Bibyan"

@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)