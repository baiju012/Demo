from flask import Flask, render_template, send_file

app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('demoindex.html')

# Custom error handler for all exceptions
@app.errorhandler(Exception)
def handle_error(error):
    return render_template('error.html', error=error), 500

# Route to download a sample PDF file
@app.route('/download_file/<filename>')
def download_file(filename):
    return send_file(f'static/files/{filename}', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
