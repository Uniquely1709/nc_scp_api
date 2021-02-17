import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nc_scp_api",
    version="0.0.1",
    author="Janneck Denda",
    author_email="j@denda.dev",
    description="API wrapper for the netcup scp api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'suds',
    ],
    packages=setuptools.find_packages(),
)