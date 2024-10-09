import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Github-scraper",
    version="1.2",
    author="CPScript",
    description="A script to scrape GitHub repositories from accounts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CPScript/Github-scraper",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
