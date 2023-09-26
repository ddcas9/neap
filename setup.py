from setuptools import setup

setup(
    name='neap',
    version='0.1.6s',
    description='A Python wrapper for the NEAP API',
    author='Bard',
    author_email='bard@google.com',
    packages = ['neap'],
    install_requires=['requests'],
)