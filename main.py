from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

name="Terrance McGee"
role="Cloud Engineer Fellow"
phone="+1-504-874-0234"
email="info@terrancemcgee.dev"
location="New Orleans, LA, United States"


@app.route("/")
def index():
    return render_template("index.html", 
    name=name,
    role=role,
    phone=phone,
    email=email
    )

if __name__ == "__main__":
    app.run(debug=True)