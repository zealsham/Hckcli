# setuptools will save you from disutills madeness
#fall back to disutills if setuptools is absent

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# description from Readme file
with open("README.md") as file:
    Description = file.read()

setup(
    name='hckcli',

    version='0.1.0',
    description=(
        "view http://news.ycombinator.com popularly known as hacker news in your commandline"

    ),
    long_description=Description,
    author="shammah Agwor",
    author_email="shammahagwor@gmail.com",
    packages=['hckli','test'],
    install_requires=(
        'requests>=2.18.4',
        'click>=6.7'
    ),
    license='MIT'

)
