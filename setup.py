import os
import sys
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

# Point the sys Path to here.
sys.path.insert(0, HERE)


with open('README.rst', 'r', encoding='utf-8') as fh:
    DESCRIPTION = fh.read()

REQUIRES = [
        'pandas',
        'bokeh',
        ]


setuptools.setup(
        name='riotstat',
        author='',
        packages=setuptools.find_packages
        long_description=DESCRIPTION,
        url='https://github.com/subertsio/riotcrawl',
        install_requires=REQUIRES,
        python_requires='>=3',
)
