from flask import render_template,redirect, url_for, flash
from flaskblog import app
from flaskblog.forms import Registration, Login
from flaskblog.models import User, Post

posts = [
    {
        'author':'Emjay',
        'title':'Why the west rule for now',
        'content':'Cos they kinda suck',
        'date': '25th Jan, 2022'
    },
    {
        'author':'Lesley',
        'title':'Dave Expedition',
        'content':'I don\'t know my self',
        'date': '14th, Feb, 2022'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods= ['GET', 'POST'])
def login():
    form = Login()
    return render_template('login.html', title = 'Login', form=form)



@app.route('/about')
def about():
    return render_template('about.html', title = 'About Page')