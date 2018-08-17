import setuptools
from geizhals import NAME
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version="0.0.5",
    author="Julian Kahnert",
    author_email="mail@juliankahnert.de",
    install_requires=[
        'beautifulsoup4>=4.6.3',
        'requests>=2.19.1'
    ],
    description="A parser for the Geizhals.eu website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JulianKahnert/PyGeizhals",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
