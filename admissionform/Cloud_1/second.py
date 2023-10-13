from flask import Flask

app = Flask(__name__)

@app.route('/')


def welcome():
  return "welcome to Home page of Fet of Grukul Kangri"


if __name__ =='__main__':
   app.run(debug=True)