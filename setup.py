from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="micronuclai_labeling",
    version="0.0.1",
    description="GUI for labeling micronuclei.",
    url="https://github.com/SchapiroLabor/micronuclAI_labeling",
    author="Miguel Ibarra",
    author_email="c180l058j@mozmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        "numpy",
        "scikit-image",
        "matplotlib",
        "pillow",
        "matplotlib",
        "mask2bbox"
    ],
    extras_require={
        "dev": ["pytest>=3.7"],
    },
)