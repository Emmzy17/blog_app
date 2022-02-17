from crypt import methods
import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration, Login
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

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


if __name__ == '__main__':
    app.run(debug=True)