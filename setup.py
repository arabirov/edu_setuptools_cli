from setuptools import setup, find_packages

NAME = "playground"
VERSION = "0.1.0"
# put your libraries here
REQUIRES = [
    "Click>=6.6",
]

setup(
    name=NAME,
    version=VERSION,
    description="Playground project for fun",
    author_email="support@playground.com",
    url="https://example.com",
    keywords="Playground",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'playground=py:cli'
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        'Intended Audience :: System Administrators',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ])
