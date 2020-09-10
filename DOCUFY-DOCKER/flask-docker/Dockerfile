FROM python:3.7-slim



COPY requirements.txt requirements.txt
COPY Docufy /opt/

RUN pip3 install -r requirements.txt
WORKDIR /opt/

CMD ["gunicorn3", "-b", "0.0.0.0:8000", "app:app", "--workers=5"]