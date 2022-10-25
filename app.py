
from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def reg():
    return render_template('register.html')

@app.route('/register', methods=['GET',"POST"])
def register():
    return render_template('naviteja.html')
#@app.route('/')
#@app.route('/',methods=['GET',"POST"])
#def register():
 #   if request.method == "POST":
      #  userName = request.form['name']
      #  password = request.form['password']
      #  email = request.form['email']
        # return render_template('naviteja.html')
  #       return render_template('result.html' )
     
       
   # return render_template('register.html')
    

@app.route('/naviteja', methods=['GET',"POST"])
def home():
    
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        num3 = request.form.get('num3')
        num4 = request.form.get('num4')
        num5 = request.form.get('num5')
        num6 = request.form.get('num6')
        add = float(num1) + float(num2)+float(num3)+float(num4) + float(num5)+float(num6)
        return render_template('result.html', add=add)
    return render_template('naviteja.html')



@app.route('/back',methods=['POST','GET'])
def back():
    if request.method=='POST':
        return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)