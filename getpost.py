from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to this Flask app, Sunny Bibyan!"

@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')


# @app.route('/form', methods=["GET"])
# def form():
#     return render_template('form.html')

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == "POST":
#         name = request.form.get('name')  # Corrected this line
#         return f"Form submitted! Hello, {name}"
#     return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        name = request.form.get('name')  # Corrected this line
        return f"Form submitted! Hello, {name}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
