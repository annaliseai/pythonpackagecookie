#!/bin/bash
# Run unittests

set -eo

export LANG=en_AU.utf8

/opt/python/cp37-cp37m/bin/pip install -r requirements.txt
/opt/python/cp37-cp37m/bin/pytest -v