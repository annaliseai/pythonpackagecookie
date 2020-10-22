#!/bin/bash
# Build wheel 

set -eo

export LANG=en_AU.utf8

# Install zip for artifacts
yum install -y zip

cp pip.conf /etc/pip.conf

/opt/python/cp37-cp37m/bin/pip install -r requirements.txt
/opt/python/cp37-cp37m/bin/python setup.py bdist_wheel

# Upload the package to s3 if on dev or master and only if a tag is assigned
# as we are using versioneer to manage python build versions
# We use [semantic versioning](https://semver.org/)
# For master branch versions use the format x.y.z
# For develop branch versions use the format x.y.z.devA
if [[ ${BUILDKITE_TAG} != "" ]]
then

    # Upload to s3
    /opt/python/cp37-cp37m/bin/pip install s3pkgup
    /opt/python/cp37-cp37m/bin/s3pkgup --project {{ cookiecutter.project_slug.replace('_', '-') }}
fi