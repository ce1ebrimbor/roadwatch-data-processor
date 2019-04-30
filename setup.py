import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roadwatch-data-processor",
    version="0.2.3",
    author="Daniel SASU",
    author_email="daniel.sasu@mail.com",
    description="A library for processing csv files on road accidents in France.\
                 Built for Project Roadwatch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daniel-sasu/roadwatch-data-processor",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas==0.24.1',
        'numpy==1.12.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
