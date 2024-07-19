from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import time
import pandas as pd
from time import sleep

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'results'

# Asigură-te că directoarele există
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('incarcare.html')

@app.route('/run-tests', methods=['POST'])
def upload_file():
    sleep(8)
    selected_tests = request.form.getlist('tests')
    print(selected_tests)
    return send_from_directory(app.config['RESULTS_FOLDER'] , 'selected Tests.7z')



if __name__ == '__main__':
    app.run(debug="True",host="0.0.0.0", port=3000)
