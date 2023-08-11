from setuptools import setup, find_packages

setup(
    name='packme',
    version='2023.8.11.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python==4.8.0.76'
    ],
)
