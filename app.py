from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/calculate',methods=["GET","POST"])
def calculate():
    operation=request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]

    if operation == 'add':
        result=num1+num2
    elif operation == 'subtract':
        result=num1-num2
    elif operation == 'multiply':
        result=num1*num2
    else:
        result=num1/num2

    return result

if __name__ == '__main__':
    app.run(debug=True)





""" from flask import Flask
#Import 3 classes from the flask module
#app is an instance of the class Flask
#parameter is the module - special variable holding the name of the module by default it is main
app=Flask(__name__)
#Create URL using route method
app.route("/home")
def Welcome():
    return "Hello World!!!"

if __name__ == '__main__':
    app.run() """
