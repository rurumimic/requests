import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="requests-rurumimic",
    version="0.0.1",
    author="rurumimic",
    author_email="unhyop@gmail.com",
    description="Python HTTP Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rurumimic/requests",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
