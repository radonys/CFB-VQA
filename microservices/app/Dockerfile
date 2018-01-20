FROM python:2

# install required debian packages
# add any package that is required after `python-dev`, end the line with \
RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
&& rm -rf /var/lib/apt/lists/*

# install requirements
COPY src/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# set /app as working directory
WORKDIR /app

# Extras for keras weight downloads
RUN python -c "from keras.applications.vgg19 import VGG19;VGG19(weights='imagenet')"

# extras for NLTK
RUN python -c "import nltk; nltk.download('punkt')"
# copy current directory to /app
COPY . /app

# run gunicorn server
# port is configured through the gunicorn config file
CMD ["gunicorn", "--config", "./conf/gunicorn_config.py", "src:app"]
