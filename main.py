import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from eye_tracking import fun
from hand.dataset.test import gesture
from speak import speech
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/start_eye_tracking')
def emotion():
   
    fun()
    return redirect(url_for('main'))


@app.route('/handgesture')
def handgesture():
   
    gesture()
    return redirect(url_for('main'))

@app.route('/speech_rec')
def speechfun():
   
    speech()
    return redirect(url_for('main'))
if __name__ == "__main__":
    app.run(debug=True,port=5002)










