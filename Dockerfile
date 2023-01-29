FROM python:3.10
COPY . /app
RUN pip install -r /app/requirements.txt
CMD python /app/app.py
