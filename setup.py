from setuptools import setup


setup(
    name='ontzia',
    version='0.1.1',
    packages=['ontzia'],
    install_requires=['flask', 'gunicorn'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
