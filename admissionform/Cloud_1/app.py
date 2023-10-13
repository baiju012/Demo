from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def health_insurance_form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        phone_number = request.form['phone_number']
        height = request.form['height']
        mark_12th = request.form['mark_12th']
        submitted = True
    
        #Pass the form data to the template
        return render_template('index.html',
                               name=name,
                               age=age,
                               phone_number=phone_number,
                               height=height,
                               mark_12th=mark_12th,
                               submitted=submitted
                               )
    
    
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)