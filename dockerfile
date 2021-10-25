FROM python:slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m pip install tortoise-orm

COPY . .

CMD ["uvicorn" , "app.main:app", "--reload", "--port","8002"]