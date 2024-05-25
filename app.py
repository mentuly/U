from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        data[name] = email
        return redirect(url_for('index'))

@app.route('/other_form')
def other_form():
    return render_template('other_form.html')

@app.route('/other_form_data', methods=['POST'])
def other_form_data():
    if request.method == 'POST':
        other_data = request.form['other_data']
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)