#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Run: python setup.py sdist upload
"""
import os
import sys

from pip.req import parse_requirements
from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

VERSION = '0.0.1'

sys.path.append(os.path.join(PROJECT_DIR, 'leonardo'))


install_reqs = parse_requirements(
    os.path.join(PROJECT_DIR, 'requirements.txt'))

reqs = [str(ir.req) for ir in install_reqs]


setup(name='django-leonardo',
      version=VERSION,
      url='https://github.com/django-leonardo/django-leonardo.git',
      author="Michael Kuty & Ales Komarek",
      author_email="mail@majklk.cz",
      description="A framework for fast building modern web \
                   applications with Django and Horizon",
      long_description=open(os.path.join(PROJECT_DIR, 'README.rst')).read(),
      keywords="CMS, Django, Horizon, E-commerce, AngularJS, React, Bootstrap 3",
      license=open(os.path.join(PROJECT_DIR, 'LICENSE')).read(),
      platforms=['any'],
      package_dir={'': 'leonardo'},
      packages=find_packages('leonardo', exclude=['tests', 'test']),
      include_package_data=True,
      install_requires=reqs,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.7',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development :: Libraries :: Application Frameworks'],
      zip_safe=False,
      )