import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="colliderfeed",
    version="0.0.1",
    description="Data feed for Intech Supercollider contest",
    long_description=README,
    long_description_content_type="text/markdown",
    url="www.3za.org/collider",
    author="microprediction",
    author_email="info@3za.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["rediz"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["asyncio","aiohttp", "requests","pathlib","retrying"],
    entry_points={
        "console_scripts": [
            "rediz=rediz.__main__:main",
        ]
     },
     )