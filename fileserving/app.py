from flask import Flask, render_template, send_file

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def display_text_file():
    with open('static/sample..txt', 'r') as file:
        text_content = file.read()
    
    return render_template('index.html', content=text_content)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = 'static/file/file.pdf'  # Replace with the actual path to your files
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
