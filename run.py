import os
import json
from flask import Flask  # imports Flask class
from flask import render_template  # imports render_template function
from flask import request  # imports request functionality from flask
from flask import flash  # imports flash functionality

if os.path.exists('env.py'):
    import env

app = Flask(__name__)  # creates instance of Flask class, stores in app
#  the first argument of the Flask class is the name of the application module - __name__

app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')  # app.route decorator, the / signifies the root directory
# When we browse to the root directory, the index function is triggered
def index():
    # return "hello world"  # returns simple plain text
    # return "<h1>Hi there!</h1>"  # returns a h1 element
    return render_template('index.html')  # returns the content of an HTML file
    # the index.html file must be in a folder named templates


@app.route('/about')
def about():
    data = []  # initialises an empty array
    with open("data/squad.json", "r") as json_data:
        data = json.load(json_data)
    return render_template('about.html', page_title='About', squad=data)
    # render_template looks in the templates folder
    #page_title holds a string, and inserts that string into the double curly braces on each page that contain page_title
    #This can be used to insert text from the run.py file rather than typing it out in the HTML file


@app.route('/about/<member_name>')  # the angle brackets here have meaning - they will pass in data from the URL path
def about_member(member_name):
    member = {}
    with open("data/squad.json", "r") as json_data:
        data = json.load(json_data)  # note that this syntax is identical to the above
        for object in data:
            if object['url'] == member_name:
                member = object
    #return "<h1>" + member['name'] + "<h1>"
    # This is very clever - /about/<member_name> does not exist as a defined file, but the HTML is being created in-situ
    # In this case, it is being used to show profiles of individual squad members
    return render_template('member.html', member=member)
    # the first 'member' here is the variable name being passed in, and the second is the member object above


@app.route('/contact', methods=['GET', 'POST'])  # methods must be used here to specify form submission methods
def contact():
    if request.method == 'POST':
        print(request.form)  # prints an list of lists, containing the values of the name attributes and the entered information
        print(request.form.get('name'))  # prints only the name that was entered, using the get method
        flash('Thanks {} , you submitted the form successfully'.format(request.form.get('name')))

    return render_template('contact.html', page_title='Contact')
    # render_template looks in the templates folder
    #page_title holds a string, and inserts that string into the double curly braces on each page that contain page_title
    #This can be used to insert text from the run.py file rather than typing it out in the HTML file


@app.route('/careers')
def careers():
    return render_template('careers.html', page_title='Careers')
    # render_template looks in the templates folder
    #page_title holds a string, and inserts that string into the double curly braces on each page that contain page_title
    #This can be used to insert text from the run.py file rather than typing it out in the HTML file


@app.route('/list')
def list_page():  # ensure this function name is the same as the name inside the url_for in any anchor tags
    return render_template('list.html', page_title='List', list_of_numbers=[1, 2, 3])


if __name__ == '__main__':  # main is the name of the default module in Python
    app.run(  # runs app using he arguments below
        host=os.environ.get('IP', '0.0.0.0'),  # IP address
        port=int(os.environ.get('PORT', '5000')),  # port number, 5000 is a common port
        debug=True  # this should be set to true for development and false for production 
        # debug = true allows arbitrary code to be run, which is a security flaw
    )

#  python3 run.py runs the program - the contents of the index function are displayed in an HTML page as plain text