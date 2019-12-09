FROM python:latest

ADD app.py .
ADD requirements.txt .

WORKDIR .

RUN pip3 install -r requirements.txt

EXPOSE 1234

CMD ["python3", "app.py"]
