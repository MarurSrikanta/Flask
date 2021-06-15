
#integrate HTML with flask(Jinja2)
#HTTP verb GET and POST

from flask import Flask, redirect, render_template,url_for,request
#render_template for rendering HTML page


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
#to use render_template we have to create another folder templates

 #render_template('index.html') #calling index.html

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('results.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return 'Candidate failed and scored '+str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result = ''
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

#result checker HTML page
@app.route('/submit',methods=['POST','GET']) #'/submit' should be same as in index.html page
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
    res = ''
    if total_score>=50:
        res='success'
    else:
        res='fail'
    return redirect(url_for(res,score=total_score))


if __name__=='__main__':
    app.run(debug=True)