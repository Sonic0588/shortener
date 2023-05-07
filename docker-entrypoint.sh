#!/bin/bash

python3 -m debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --use-colors --reload
