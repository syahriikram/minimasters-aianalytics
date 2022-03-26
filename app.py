from flask import Flask
app = Flask(__name__)

from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        num = float(request.form.get("rates"))
        print(num)
        model = joblib.load("DBS_Reg")
        pred = model.predict([[num]])
        print(pred)
        s = "Predicted DBS Share Price : " + str(pred)
        print(s)
        return(render_template("index.html", result = s))
    else:
        return render_template("index.html", result ="DBS Share Price Prediction")

if __name__ == '__main__':
     app.run()
