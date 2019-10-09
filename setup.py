#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import versioneer
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'versioneer>=0.18',
]

setup_requirements = ['pytest-runner', ]

test_requirements = [
    'pytest>=5.1.2',
    'pytest-cov>=2.7.1',
]

setup(
    name='pythonpackagecookie',
    keywords='pythonpackagecookie',
    author="Ben Johnston",
    author_email='ben.johnston@harrison.ai',
    python_requires='>=3.6.*',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',

    ],
    description='Cookiecutter template for Harrison.ai Python Packages',
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
#    packages=find_packages(include=['dicom_anon']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://bitbucket.org/harrison-ai/pythonpackagecookie/',
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
