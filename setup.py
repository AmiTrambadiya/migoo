from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in migoo/__init__.py
from migoo import __version__ as version

setup(
	name="migoo",
	version=version,
	description="migoo",
	author="migoo",
	author_email="ami@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
