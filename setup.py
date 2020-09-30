import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zenora",
    version="0.0.34",
    author="K.M Ahnaf Zamil",
    author_email="ahnafzamil@protonmail.com",
    description="A modern Discord REST API wrapper that allows you to access the data without running a bot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahnaf-zamil/zenora",
    packages=["zenora", "zenora.impl", "zenora.base", "zenora.utils"],
    install_requires=["requests", "typing", "pre-commit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
