

import decimal
import time

from flask import Flask, render_template, request, session, flash, redirect

app = Flask(__name__)
app.secret_key = 'fhdgsd;ohfnvervneroigerrenverbner32hrjegb/kjbvr/o'

@app.route('/')

@app.route('/form')
def form() -> 'html':
    return render_template('form.html',
                           title="Visa Application Checker")


@app.route('/processForm', methods=['POST'])
def process_form() -> 'html':
    ### Do all form processing here e.g adding up points etc.
    return render_template('result.html',
                               title="Visa Prediction")

if __name__ == '__main__':
    app.run(debug=True)
