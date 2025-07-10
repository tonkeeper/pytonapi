import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytonapi",
    version="0.5.0",
    author="nessshon",
    description="Provide access to indexed TON blockchain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tonkeeper/pytonapi/",
    packages=setuptools.find_packages(include=["pytonapi", "pytonapi.*"]),
    install_requires=[
        "aiohttp>=3.9.0,<=3.12.2",
        "pydantic>=2.4.1,<=2.11.5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        "": ["*py.typed"],
    },
)
