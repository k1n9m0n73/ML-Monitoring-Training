from setuptools import find_packages, setup

setup(
    name="wine_quality_model",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[],
)
