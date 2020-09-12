FROM python:3.7.3-slim-stretch

WORKDIR /usr/src/app

EXPOSE 8000 9200

COPY * /usr/src/app/
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /usr/src/app

CMD [ "python3", "main.py" ]