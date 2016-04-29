from setuptools import setup


long_description = """
API Wrapper to access the Open Source License API

The Open Source API can be found at https://api.opensource.org, and
some (very brief!) documentation can be found in the API server documentation
(https://github.com/OpenSourceOrg/api/blob/master/doc/endpoints.md).
"""

setup(
    name="opensource",
    version="1.0.2",
    packages=[
        'opensource',
        'opensource.licenses',
    ],
    author="Paul Tagliamonte",
    author_email="paultag@opensource.org",
    long_description=long_description,
    description="Query the Open Source License API",
    license="MIT",
    install_requires=[
        "requests",
    ],
    url="",
    platforms=['any']
)
