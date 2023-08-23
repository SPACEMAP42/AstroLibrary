from setuptools import find_packages, setup

setup(
    name='astrolibrary',
    version='0.1.4',
    packages=find_packages(),
    install_requires=['requests', 'sgp4', 'numpy'],
    author='Spacemap',
    author_email='contact@spacemap42.com',
    description='astrolibrary version 0.1.4',
    url='https://github.com/SPACEMAP42/AstroLibrary',
)