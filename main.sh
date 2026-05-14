#!/bin/bash

cd src
python3 main.py "/static_site_generator/"
cd ../docs && python3 -m http.server 8888