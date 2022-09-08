from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect

app = Flask(__name__)

import sys
import os

@app.route('/', methods=['GET', 'POST'])

def Menu():
    return render_template("home.html")

if _name_ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=8001)
