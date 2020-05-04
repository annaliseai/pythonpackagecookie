#!/bin/bash
# Build wheel 

set -eo

export LANG=en_AU.utf8

# Install zip for artifacts
yum install -y zip

/opt/python/cp37-cp37m/bin/pip install -r requirements.txt
/opt/python/cp37-cp37m/bin/python setup.py bdist_wheel

if [ ${BUILDKITE_BRANCH} == "master" ]
then

    # Upload to s3
    /opt/python/cp37-cp37m/bin/pip install --extra-index-url \
        http://pypi-prod-annalise-ai.s3-website-ap-southeast-2.amazonaws.com/simple/ \
        --trusted-host pypi-prod-annalise-ai.s3-website-ap-southeast-2.amazonaws.com s3pkgup

    /opt/python/cp37-cp37m/bin/s3pkgup --project {{ cookiecutter.project_name }}

fi