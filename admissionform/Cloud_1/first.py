from flask import Flask

g = Flask(__name__)

@g.route('/')

def welcome():
  return "welcome to Home page of Fet"


if __name__ == '__main__':
   g.run(debug=False)