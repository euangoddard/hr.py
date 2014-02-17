from setuptools import setup

version = '0.1'

setup(
    name='hr',
    version=version,
    description='Horizontal rule for your terminal',
    author='Euan Goddard',
    url='http://github.com/euangoddard/hr.py',
    license='',
    py_modules=['hr'],
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    hr = hr:cli
    """,
    )
