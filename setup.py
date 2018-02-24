from setuptools import setup


setup(
    name='ontzia',
    version='0.1.1',
    packages=['ontzia'],
    install_requires=['flask', 'flask-restful', 'gunicorn', 'icalendar', 'pytz'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
