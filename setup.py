from setuptools import setup, find_packages

setup(
	name="medical_chabot",
	version="0.0.1",
	description="Medical chatbot project package",
	package_dir={"": "src"},
	packages=find_packages(where="src"),
	include_package_data=True,
)
