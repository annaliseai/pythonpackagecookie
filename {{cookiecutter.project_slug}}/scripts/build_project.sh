#!/bin/bash
# Build wheel 

set -eo

export LANG=en_AU.utf8

# Install zip for artifacts
yum install -y zip

cp pip.conf /etc/pip.conf

/opt/python/cp37-cp37m/bin/pip install -r requirements.txt
/opt/python/cp37-cp37m/bin/python setup.py bdist_wheel

if [ ${BUILDKITE_BRANCH} == "master" ]
then

    /opt/python/cp37-cp37m/bin/s3pkgup --project {{ cookiecutter.project_slug.replace('_', '-') }}

fi