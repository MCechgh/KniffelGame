"""
pyEA
"""
import setuptools
from os import path

# Get the long description from the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

# Get the version from the version.py file   
with open(path.join('Kniffel', 'version.py'), 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[-1].strip().strip('"')
            break

setuptools.setup(
    name='Kniffel',

    version=version,

    # Author details
    author="MCechgh",
    author_email="marcel.cech@t-online.de",

    description="Small Kniffel Game.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # What does your project relate to?
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    install_requires=['Pillow>=9.0.0'],

    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
