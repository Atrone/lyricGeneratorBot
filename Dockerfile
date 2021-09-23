FROM python:3.9

RUN pip install discord lyricsgenius pymongo pymongo[srv]

COPY . .


