![ Code For Beer Event Logo](hackathon.jpg "FYI: Our team had a total of 12 beers")
# Visual Question Answering

Based on the [VQA challenge](http://www.visualqa.org/) and [paper](http://arxiv.org/pdf/1505.00468v6.pdf), this is just a simple implementation of a pretrained model on a flask server.<br>
online demo: [Hasura](https://app.debris23.hasura-app.io/) ( can only run images below 1Mb due to server limits)<br>
**Note: This is a python 2 program**

## Installation

0. Install dependencies:
```python2
pip install -r requirements.txt
```
1. Download weights from here: [G-Drive](https://drive.google.com/file/d/0B3b69xdtpDT8U2dwajNKOEhUWUU/view?usp=sharing) and add it to `resources` folder.
2. Download nltk punkt data (for tokenization) using `python -c "import nltk; nltk.download('punkt')"`.
3. VGG19 model weights are needed which will start downloading automatically once the `server.py` runs, or can be downloaded using `python -c "from keras.applications.vgg19 import VGG19;VGG19(weights='imagenet')"`. Note that this will happen only once
4. Run the demo.
```python2
FLASK_APP=server.py flask run -h 0.0.0.0 -p 8000
```

# Credits
This code and weights are based on [@anantzoid](https://github.com/anantzoid)'s VQA [code](https://github.com/anantzoid/VQA-Keras-Visual-Question-Answering).
