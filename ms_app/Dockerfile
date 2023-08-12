# Use an official Python image as the base image
FROM python:3.9
COPY . /app
WORKDIR /app

EXPOSE 5000
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python app.py