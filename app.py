from flask import Flask, render_template, request, redirect

app = Flask(_name_)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit_form', methods=['GET','POST'])
def submit():
    # Handle form submission logic here
    return redirect(url_for('index'))

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=2000, debug=True)
