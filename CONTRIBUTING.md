# Contributing to Zenora

When contributing to this repository, please first discuss the change you wish to make via issue,
messaging, or any other method with the owners of this repository before making a change.

Please note we have a [Code of Conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Contributing Process

We recommend that you make a fork of our GitHub repository in order to contribute. Then you can clone your fork onto your computer

1. Run `pip install -r dev-requirements.txt` to install all the development dependencies.
2. Run `pre-commit install` to install the pre-commit hooks.
3. Ensure any install/build dependencies and test files are in the `.gitignore` file or removed before doing a
   pull request.
4. Run `nox` to run all the pipelines
5. Update the documentation and changelog in the `docs/` folder with details of changes to the interface, this
   includes new environment variables, exposed ports, useful file locations and container parameters.
6. Increase the version numbers in any examples files, the README.md, setup.py and documentation to the new version that this pull request would represent.
7. Push to your fork, and make a pull request.
