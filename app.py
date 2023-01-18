#importing the modules

from flask import Flask,render_template,request
import joblib

model = joblib.load('spam_model.pkl')

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        messages = request.form.get('messages')
        a = str(messages)
        a = a.lower()
        output = model.predict([a])

        if output==[0]:
            result = "This Message is Not a SPAM Message."
        else:
            result = "This Message is a SPAM Message."

        return render_template("index.html", messages=messages,result=result)
    else:
        return render_template("index.html")

if __name__ =='__main__':
    app.run(debug=True)



