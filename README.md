# Step Tracking Server

python3 -m virtualenv python-api

source python-api/bin/activate

pip install -r requirements.txt

python3 -m pytest spec

python3 -m pytest -s spec/test_ws_api.py

python3 -m uvicorn main:app --reload --port 8001

pip freeze > requirements.txt