import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="XamPy",
    version="0.1.3",
    author="Max Paul",
    author_email="maxkpaul21@gmail.com",
    description="A Data Science Package written in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requres=[
        'nltk',
        'pandas',
        'vaderSentiment',
        'numpy',
        'sklearn',
        'textblob',
        'sklearn',
        'datetime'
    ]
)