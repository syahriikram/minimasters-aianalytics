from flask import Flask
app = Flask(__name__)

from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        num = float(request.form.get("purchases"))
        print(num)
        card = float(request.form.get("suppcard"))
        print(card)
        cart_model = joblib.load("CART")
        rf_model = joblib.load("RF")
        xgb_model = joblib.load("GBC")

        cart_pred = cart_model.predict([[num,card]])
        rf_pred = rf_model.predict([[num,card]])
        xgb_pred = xgb_model.predict([[num,card]])

        return(render_template("index.html", result1 = cart_pred, result2 = rf_pred, result3 = xgb_pred))
    else:
        return render_template("index.html", result ="GET METHOD")

if __name__ == '__main__':
     app.run()
