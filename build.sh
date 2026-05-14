#!/bin/bash

BASEPATH=${GITHUB_PAGES_BASEPATH:-"/static_site_generator/"}
python3 src/main.py "$BASEPATH"

echo "Site built successfully into /docs folder!"