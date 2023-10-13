from flask import Flask

app = Flask(__name__)

@app.route('/')


def welcome():
  return "welcome to Home page of Fet of Grukul Kangri"


@app.route('/Baiju')

def massage():
  return "welcome to on baiju page"

@app.route('/student')

def student():
  return "welcome to on student page"


if __name__ =='__main__':
   app.run(debug=True)