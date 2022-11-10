from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def render_login(accountok=True):
    if accountok==True:
        return render_template("login.html",message="")
    else:
        return render_template("login.html",message="Username/Password is worng!!") 


@app.route("/signin",methods= ['POST'])
def checkLogin():
    email = request.form['email']
    pwd = request.form['password']
    if(email=="hello@abc.com" and pwd=="hello@123"):
        return render_template("website.html")
    else:
        return render_login(False)


if __name__=="__main__":
    app.run(debug=True)