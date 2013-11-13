import os
from setuptools import setup, find_packages

# package meta info
NAME = "hongqncfg"
VERSION = "0.1"
DESCRIPTION = "hongqn's occupy config"
AUTHOR = "Qiangning Hong"
AUTHOR_EMAIL = "hongqn@gmail.com"
LICENSE = "BSD"
URL = ""
KEYWORDS = ""
CLASSIFIERS = []

# package contents
MODULES = []
PACKAGES = find_packages(exclude=['tests.*', 'tests', 'examples.*', 'examples'])
ENTRY_POINTS = """
"""

# dependencies
INSTALL_REQUIRES = ['occupy']
TESTS_REQUIRE = ['nose']
TEST_SUITE = 'nose.collector'

here = os.path.abspath(os.path.dirname(__file__))


def read_long_description(filename):
    path = os.path.join(here, filename)
    if os.path.exists(path):
        return open(path).read()
    return ""

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read_long_description('README.rst'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    py_modules=MODULES,
    packages=PACKAGES,
    install_package_data=True,
    zip_safe=False,
    entry_points=ENTRY_POINTS,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    test_suite=TEST_SUITE,
)
