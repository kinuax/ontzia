from setuptools import setup


setup(
    name='ontzia',
    version='0.1.0',
    packages=['ontzia'],
    install_requires=['flask'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
