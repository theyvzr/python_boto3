FROM python:3-alpine
COPY . .
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3", "basic_flask.py"]
