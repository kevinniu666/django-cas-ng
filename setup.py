#!/usr/bin/env python

from __future__ import absolute_import

import codecs

from setuptools import setup

with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    author='Ming Chen',
    author_email='mockey.chen@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ],
    description='CAS 1.0/2.0 client authentication backend for Django (inherited from django-cas)',
    keywords=['django', 'cas', 'cas2', 'cas3', 'client', 'sso', 'single sign-on', 'authentication', 'auth'],
    license='BSD',
    long_description=readme,
    name='django-cas-ng',
    packages=['django_cas_ng', 'django_cas_ng.management', 'django_cas_ng.management.commands', 'django_cas_ng.migrations'],
    package_data = {
        'django_cas_ng': ['locale/*/LC_MESSAGES/*',],
    },
    url='https://github.com/mingchen/django-cas-ng',
    #bugtrack_url='https://github.com/mingchen/django-cas-ng/issues',  # not support this key
    download_url ='https://github.com/mingchen/django-cas-ng/releases',
    version='4.0.0',
    python_requires=">=3.5",
    install_requires=[
        'Django>=2.0',
        'python-cas>=1.4.0',
    ],
    zip_safe=False,  # dot not package as egg or django will not found management commands
)
