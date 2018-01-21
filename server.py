from flask import Flask
app = Flask(__name__)
import os
from flask import jsonify
from flask import render_template,request
from VQA import predict
import sys
import random
import string
UPLOAD_FOLDER = 'static'
@app.route("/", methods = ['GET', 'POST'])
def home():
    print "Hello"
    print request.args,request.form
    if request.method == 'POST':
        # print request.args,request.form
        if "question" in request.form:
            print "POST FORM"
            file1 = request.files['file']
            ques = request.form["question"]
            temp = os.path.join(UPLOAD_FOLDER, ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])+'.jpg')
            file1.save(temp)
            result = predict(temp,ques)
            os.remove(temp)
            return jsonify(result=result,success=True)
        else:
            print "NO question came"
            return "oops"
    else:
        return render_template('index.html')
sys.stdout.flush()
