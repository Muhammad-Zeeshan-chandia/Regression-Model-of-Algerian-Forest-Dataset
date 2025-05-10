from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app=application

@app.route('/')
def hello():
    return "Hello Army"

if __name__ == '__main__':
    app.run(debug=True)
