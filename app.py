from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/calendar")
def calendar():
    return "Here's what you have scheduled!"
    
if __name__ == "__main__":
    app.run(debug=True)