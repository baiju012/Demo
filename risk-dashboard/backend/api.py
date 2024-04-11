from flask import Flask, request, jsonify
from database import get_risks_data

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Risk Dashboard API'

@app.route('/api/risks', methods=['GET'])
def get_risks():
    filters = {'topics': ['gas']}
    risks = get_risks_data(filters)
    return jsonify(risks)

if __name__ == '__main__':
    app.run(debug=True)
