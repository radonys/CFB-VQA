from src import app
# from flask import jsonify
from flask import render_template,request
from VQA import predict
import sys
UPLOAD_FOLDER = '/path/to/the/uploads'
@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        file1 = request.files['file']
        ques = request.post["question"]
        temp = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
        print temp
        file1.save(temp)
        print file1,type(file1)
        result = predict(temp,ques)
        print result
        sys.stdout.flush()
        return render_template('index.html',result=result)

sys.stdout.flush()
# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
