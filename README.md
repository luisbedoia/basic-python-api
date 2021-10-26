# Step Tracking Server

git clone https://github.com/luisbedoia/basic-python-api.git

cd basic-python-api

python3 -m virtualenv python-api

source python-api/bin/activate

pip install -r requirements.txt

python3 -m pytest spec

python3 -m pytest -s spec/test_ws_api.py

python3 -m uvicorn main:app --reload --port 8001

pip freeze > requirements.txt

docker-compose up --build --force-recreate
docker-compose -f docker-compose.test.yml up --build --force-recreate
docker-compose rm -fvs

<!-- # Step Tracking Server

A simple example of using Fast API in Python.


## Clone the project

```
git clone https://github.com/luisbedoia/basic-python-api.git
```

## Run local

### Create a virtual environment and activate it
```
cd basic-python-api

python3 -m virtualenv python-api

source python-api/bin/activate
```
### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
python3 -m uvicorn app.main:app --reload --port 8002
```

### Run test

```
python3 -m pytest spec
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

### Run test

```
docker-compose exec app pytest test/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server

```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
``` -->