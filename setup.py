#!/usr/bin/env python
from setuptools import setup



with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='annual_report',
    version='0.0.2',
    packages=['annual_report'],
    license='MIT license',
    description="the objectives of this project, is to retrieve all annual report documents on a given website",
    long_description= long_description,
    long_description_content_type="text/markdown",

    
    url='https://github.com/darixsamani/annual_report',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
    python_requires='>=3.6',                
    py_modules=["annual_report"],             
    package_dir={'':'./src'},     
    install_requires=[
        'beautifulsoup4==4.12.2',
        'bs4==0.0.1',
        'certifi==2023.7.22',
        'charset-normalizer==3.2.0',
        'exceptiongroup==1.1.2',
        'idna==3.4',
        'iniconfig==2.0.0',
        'packaging==23.1',
        'pluggy==1.2.0',
        'pytest==7.4.0',
        'requests==2.31.0',
        'soupsieve==2.4.1',
        'tomli==2.0.1',
        'urllib3==2.0.4',
    ],
    
)
