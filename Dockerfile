FROM python:3-alpine
WORKDIR /app
COPY . .
COPY requirements.txt requirements.txt
RUN pip install logging
RUN pip install -r requirements.txt
CMD ["python3", "flask_app.py"]
