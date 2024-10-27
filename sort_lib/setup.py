from setuptools import setup, find_packages

setup(
    name='sort-lib',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},  # Tells setuptools to look in the src directory
    install_requires=[
        
    ],
)
