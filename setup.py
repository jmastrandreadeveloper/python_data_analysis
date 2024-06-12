from setuptools import setup, find_packages

setup(
    name='data_analysis_framework',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
    ],
)
