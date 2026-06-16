#! /usr/bin/bash

source .venv/bin/activate
gunicorn life_blood_network.wsgi
