#building the url dynamically
#variable rules and url building

from flask import Flask,redirect,url_for
#redirect to redirect to a particular page if a condition is satisfied
#url_for to create url dynamically

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to pycharm'

@app.route('/success/<int:score>') #score in int format. <score> will be in str format
def success(score):
    return 'Person has passed: '+ str(score)

@app.route('/fail/<int:score>') #score in int format. <score> will be in str format
def fail(score):
    return 'Person has failed: '+ str(score)

###result checker
@app.route('/result/<int:marks>')
def result(marks):
    result = ''
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)