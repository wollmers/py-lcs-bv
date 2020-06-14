import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lcs-bv-wollmers", # Replace with your own username
    version="0.0.1",
    author="Helmut Wollmersdorfer",
    author_email="helmut@wollmersdorfer.at",
    description="LCS algorithm using bit vectors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wollmers/py-lcs-bv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
