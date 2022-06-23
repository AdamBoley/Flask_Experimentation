import os
from flask import Flask  # imports Flask class
from flask import render_template  # imports render_template function

app = Flask(__name__)  # creates instance of Flask class, stores in app
#  the first argument of the Flask class is the name of the application module - __name__


@app.route('/')  # app.route decorator, the / signifies the root directory
# When we browse to the root directory, the index function is triggered
def index():
    # return "hello world"  # returns simple plain text
    # return "<h1>Hi there!</h1>"  # returns a h1 element
    return render_template('index.html')  # returns the content of an HTML file
    # the index.html file must be in a folder named templates


@app.route('/about')
def about():
    return render_template('about.html')
    # render_template looks in the templates folder


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/careers')
def careers():
    return render_template('careers.html')


if __name__ == '__main__':  # main is the name of the default module in Python
    app.run(  # runs app using he arguments below
        host=os.environ.get('IP', '0.0.0.0'),  # IP address
        port=int(os.environ.get('PORT', '5000')),  # port number, 5000 is a common port
        debug=True  # this should be set to true for development and false for production 
        # debug = true allows arbitrary code to be run, which is a security flaw
    )

#  python3 run.py runs the program - the contents of the index function are displayed in an HTML page as plain text