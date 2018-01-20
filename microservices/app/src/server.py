from src import app
# from flask import jsonify
from flask import render_template,request
from VQA import predict
UPLOAD_FOLDER = '/path/to/the/uploads'
@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        file1 = request.files['file']
        temp = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file1.save(temp)
        print file1,type(file1)
        result = predict(temp)
        return render_template('index.html',result=result)


# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
