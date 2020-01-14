from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'me',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Ivan',
        'title': 'Blog Post 2',
        'content': 'Blog post 2',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
#  2nd route for same webpage
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

#  new webpage
@app.route('/about')
def about():
    return render_template('about.html', title='About')

#  for running as 'python flaskblog.py'
#  instead of 'flask run' w/ setting local variable through set/export
if __name__ == '__main__':
    app.run(debug=True)