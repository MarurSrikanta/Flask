from flask import Flask,request, jsonify,render_template

app = Flask(__name__)

@app.route('/via_postman',methods=['POST'])
def math_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if (operation=='add'):
            r = num1+num2
            result='Sum of ' + str(num1)+ ' and ' +str(num2)+ ' is ' + str(r)
        if (operation=='subtract'):
            r=num1-num2
            result='Difference between ' + str(num1)+ ' and ' +str(num2)+ ' is ' + str(r)
        if (operation== 'multiplication'):
            r = num1*num2
            result='Product of '+str(num1)+' and '+str(num2)+' is ' + str(r)
        if (operation=='division'):
            r = num1/num2
            result='Quotient of '+str(num1)+' divided by '+str(num2)+' is ' + str(r)
        return jsonify(result)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_operation():
    if request.method=='POST':
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if (operation=='add'):
            r=num1+num2
            result='the sum of ' + str(num1)+ ' and ' +str(num2)+ ' is ' + str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference between ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)

if __name__=='__main__':
    app.run(debug=True)