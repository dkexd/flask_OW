from flask import Flask
app = Flask(__name__)

@app.route('/')
#  2nd route for same webpage
@app.route('/home')
def hello_world():
    return '<h1>Hello, World!</h1>'

#  new webpage
@app.route('/about')
def about():
    return '<h1>About</h1>'

#  for running as 'python flaskblog.py'
#  intead of 'flask run' w/ setting loacl variable through set/export
if __name__ == '__main__':
    app.run(debug=True)