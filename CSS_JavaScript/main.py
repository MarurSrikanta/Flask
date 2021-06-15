
#integrate HTML with flask(Jinja2)
#HTTP verb GET and POST

##Jinja2 template for integrating HTML with data source
'''

{%...%} conditions, for loops
{{...}} expressions to print output
{#...#} for comments
'''

from flask import Flask, redirect, render_template, url_for, request
#render_template for rendering HTML page


app = Flask(__name__)

#to use render_template we have to create another folder templates

#render_template('index.html') #calling index.html

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)


@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is " + str(score)


### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))


### Result checker submit html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
    res = ""
    return redirect(url_for('success', score=total_score))


if __name__ == '__main__':
    app.run(debug=True)


