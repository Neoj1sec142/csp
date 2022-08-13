from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '6481e35c4a172213fdc7eaafe560ec4f'

posts = [
    {
        'author': 'Neo Skeleton',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog post 2',
        'content': 'senconsd post content',
        'date_posted': 'April 20, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)