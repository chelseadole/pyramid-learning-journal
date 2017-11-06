"""Setup."""

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid >= 1.9a',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2'
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
    'tox'
]

setup(
    name='chelsea_pyramid_learning_journal',
    version='0.0',
    description='chelsea_pyramid_learning_journal',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Chelsea Dole',
    author_email='chelseadole@gmail.com',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = chelsea_pyramid_learning_journal:main',
        ],
        'console_scripts': [
            'initializedb = chelsea_pyramid_learning_journal.scripts.initializedb:main',
        ],
    },
)
