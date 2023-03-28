
from flask import Flask, render_template, request , redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/dash')
def dash():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
