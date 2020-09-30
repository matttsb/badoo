#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages,setuptools
with open('README.rst') as readme_file:
    readme = readme_file.read()

long_description=readme
with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'selenium','BeautifulSoup4','lxml']


setuptools.setup(
    name="badoo", # Replace with your own username
    version="1.3.1",
    author="Matt Burke",
    author_email='matttsburke@gmail.com',
    description="Remotely control badoo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/matttsb/badoo',
    packages=setuptools.find_packages(exclude=['tests*']),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
setup(
    author="Matt Burke",
    author_email='matttsburke@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="remotely control badoo",
    entry_points={
        'console_scripts': [
            'badoo=badoo.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='badoo',
    name='badoo',
    packages=find_packages(exclude=['tests*'],include=['badoo', 'badoo.*']),
    url='https://github.com/matttsb/badoo',
    version='1.3.2',
    zip_safe=False,
)
