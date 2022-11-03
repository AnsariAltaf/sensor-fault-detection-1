'''
This is required to create packages.
Inside setup.py file we will write code that will help to install sensor package 
so that it can be shared or published.
'''

from setuptools import find_packages,setup
from typing import List

#def get_requirements()->List[str]:...
"""
    This function will return the list of requirements.
"""
   # requirement_list:List[str]=[]

"""
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.

    """
    #return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="altaf",
    author_email="ansarialtaf23.aa@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo==4.2.0"],              #   get_requirements(),
)

