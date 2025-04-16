from setuptools import setup, find_packages

setup(
    name='etl-framework-iceberg',
    version='0.1',
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    entry_points={
        'console_scripts': [
            'etl-run = main:main'
        ]
    }
)
