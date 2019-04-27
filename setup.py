import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roadwatch-data-processor",
    version="0.1",
    author="Daniel SASU",
    author_email="daniel.sasu@mail.com",
    description="A library for processing csv files on road crashes in France. \
                 Build for Project Roadwatch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daniel-sasu/roadwatch-data-processor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
