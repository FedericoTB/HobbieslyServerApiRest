#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python ./hobserverdj/manage.py collectstatic --no-input
python ./hobserverdj/manage.py migrate
python ./hobserverdj/manage.py loaddata initial_data.json