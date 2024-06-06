#find_packages() automatically finds out all packages 
#that are used in the entire application/directory
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements from the requirements file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #replace line breaks with blanks
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            #-e . in the requirements.txt will automatically triger setup.py to run
            #so that the setup.py runs to build the packages whenever installing all the requirements
            #but we do not want in the list of requirements
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Garima Khakurel',
    author_email = 'garimakhakurel1@gmail.com',
    packages= find_packages(), #returns all folders (packages) with __init__.py
    install_requires = get_requirements('requirements.txt') #list of libraries required
)