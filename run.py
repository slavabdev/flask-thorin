import os
from flask import Flask, render_template


# Creating an instance of the class and store it in variable app
app = Flask(__name__)


# Route decorator will tell Flask what URL following function will trigger
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html", page_title='About')


@app.route('/contact')
def contact():
    return render_template("contact.html", page_title='Contacts')


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title='Careers')


# Main and name are default python modules
if __name__ == "__main__":
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', '5000')),
        debug=True  # Make debug False when submit the project
    )
