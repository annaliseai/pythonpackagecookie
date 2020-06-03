#!/bin/bash
# Run unittests

set -eo
N_WORKERS=${N_TESTING_WORKERS:-1}
export LANG=en_AU.utf8

/opt/python/cp37-cp37m/bin/pip install -r requirements.txt
/opt/python/cp37-cp37m/bin/pytest -n=${N_WORKERS} -v