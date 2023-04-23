FROM python:3.10.11-buster

COPY amenities src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "src/save_amenities.py"]
