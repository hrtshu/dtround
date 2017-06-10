
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from dtround.version import __version__

metadata = {
    'name': 'dtround',
    'packages': ['dtround'],
    'version': __version__,
    'description': 'Python module for rounding datetime/date object',
    'python_requires': '>=2.7,!=3.0.*,!=3.1.*',
    'author': 'Shuhei Hirata',
    'author_email': 'sh7916@gmail.com',
    'license': 'MIT',
    'url': 'https://github.com/hrtshu/dtround',
    'keywords': ['datetime', 'date', 'round', 'floor', 'ceil'],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
}

setup(**metadata)
