FROM python:3.13-slim

WORKDIR /the/workdir/path

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY opensource_evaluation ./opensource_evaluation

WORKDIR /the/workdir/path/opensource_evaluation

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
