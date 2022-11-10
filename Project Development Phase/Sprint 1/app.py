from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__=="__main__":
    app.run(debug=True)