from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="utils_formatter_br",
    version="0.0.1",
    author="Juan de Oliveira Farias",
    author_email="juanfarias580@gmail.com",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    python_requires='>=3.8',
)