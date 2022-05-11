from setuptools import find_packages, setup

setup(
    name='sflight-ryanair',
    author='Adrian Fusco',
    license='Apache',
    description='Used for searching flights between two'
    'airports',
    version='0.0.1',
    url='https://github.com/adrianfusco/sflight-ryanair',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['sflight = sflight.search:main']
    },
    install_requires=[
        'requests~=2.27.1'
    ]
)
