#!/bin/bash
cd /home/pi/python/supervision && source ./env/bin/activate && gunicorn --threads 5 --workers 4 --bind 0.0.0.0:8000 app:app
