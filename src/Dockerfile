FROM python:3.11.3-alpine3.17 

COPY amenities src

COPY requirements.txt requirements.txt

CMD ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python", "src/load_osm.py"]