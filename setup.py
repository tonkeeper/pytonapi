import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytonapi",
    version="0.0.8",
    author="nessshon",
    description="Provide access to indexed TON blockchain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nessshon/pytonapi/",
    packages=setuptools.find_packages(exclude="pytonapi"),
    python_requires='>=3.7',
    install_requires=[
        "aiohttp>=3.8.3",
        "libscrc>=1.8.1",
        "pydantic==1.10.4",
        "requests>=2.29.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
