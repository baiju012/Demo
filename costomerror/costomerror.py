from flask import Flask, render_template

app = Flask(__name__)

# Custom error handler for all exceptions
@app.errorhandler(Exception)
def handle_error(error):
    # Customize the error response and set the status code to 500
    return render_template('error.html', error=error), 5000000

# Catch-all route to handle undefined URLs
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # Raise an exception with your custom error message
    error_message = "This is a custom error message for undefined routes."
    raise Exception(error_message)

if __name__ == '__main__':
    app.run(debug=True)
