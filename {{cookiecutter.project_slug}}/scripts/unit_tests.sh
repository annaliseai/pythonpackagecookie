#!/bin/bash
# Run unittests

set -eo
N_WORKERS=${N_TESTING_WORKERS:-1}
export LANG=en_AU.utf8

cp pip.conf /etc/pip.conf

/opt/python/cp37-cp37m/bin/pip install -r requirements.txt

echo -e "--- Running \033[33mspecs\033[0m :pray:"
/opt/python/cp37-cp37m/bin/pytest -n=${N_WORKERS} -v
