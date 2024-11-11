### Building Url Dynamically
## Variable Rule
### Jinja2 Template Engine

### jinja Template Engine

'''
{{}} expressions to print output in html
{%....%} conditions , for loops
{#...#} this is for commits
'''




from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to this Flask app, Sunny Bibyan!"

@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        name = request.form.get('name')  # Corrected this line
        return f"Form submitted! Hello, {name}"
    return render_template('form.html')

## Variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
        
    return render_template('result.html', results=res)


## Variable rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
        
    return render_template('result.html', results=res)


if __name__ == '__main__':
    app.run(debug=True)
