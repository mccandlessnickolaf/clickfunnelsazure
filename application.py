from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://clickfunnels.com/?cf_affiliate_id=2025786&affiliate_id=2025786", code=302)
