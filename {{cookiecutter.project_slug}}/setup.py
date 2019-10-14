#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import versioneer
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=7.0',{%- endif %}
]

setup_requirements = [
    {%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %}
]

test_requirements = [
    {%- if cookiecutter.use_pytest == 'y' %}'pytest>=3',{%- endif %}
]

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='!=2.*, >=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=requirements,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://bitbucket.org/harrison-ai/{{ cookiecutter.project_slug }}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
