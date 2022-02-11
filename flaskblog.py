from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route('/about')
def about():
    return render_template('about.html', title = 'About Page')


if __name__ == '__main__':
    app.run(debug=True)