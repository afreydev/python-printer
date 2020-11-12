import pathlib
from setuptools import setup

BASE_PATH = pathlib.Path(__file__).parent
README = (BASE_PATH / "README.md").read_text()

setup(
    name="python-printer",
    version="1.0.0",
    description="Print awesome messages in your screen",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/afreydev/python-printer",
    author="Angel Rey",
    author_email="afreydev@gmail.com",
    license="MIT",
    packages=["python_printer"],
    include_package_data=True,
)
