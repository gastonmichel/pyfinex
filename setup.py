import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfinex",
    version="1.0.2",
    author="faberquisque",
    author_email="faberquisque@hotmail.com",
    description="Python wrapper for Bitfinex API v1 and v2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/faberquisque/pyfinex",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)