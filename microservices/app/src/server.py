from src import app
# from flask import jsonify
from flask import render_template,request
from VQA import predict
@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        file1 = request.files['file']
        
        print file1,type(file1)
        return render_template('index.html')


# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
