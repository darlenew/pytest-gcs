"""Setup for pytest-gcs plugin."""
from setuptools import setup


setup(
    name='pytest-gcs',
    version='0.1.0',
    description='A pytest plugin to upload reports to Google Cloud Storage',
    author='Darlene Wong',
    author_email='darlene.py@gmail.com',
    license='MIT',
    py_modules=['pytest_gcs'],
    packages=['gcp'],
    install_requires=['pytest', 'pytest-html', 'google-cloud-storage'],
    entry_points={'pytest11': ['gcs = pytest_gcs', ]},
)
