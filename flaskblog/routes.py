from flask import render_template,redirect, url_for, flash, request
from flaskblog import app,db, bcrypt
from flaskblog.forms import Registration, Login
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return  redirect(url_for(next_page)) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check your email and password', 'danger')
    return render_template('login.html', title = 'Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
@app.route('/about')
def about():
    return render_template('about.html', title = 'About Page')