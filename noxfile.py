import nox
import os

cwd = os.getcwd()


@nox.session(reuse_venv=True)
def tests(session):
    session.install("pytest")
    session.install("attrs")
    session.install("requests")
    session.run("pytest")


@nox.session(reuse_venv=True)
def mypy(session):
    session.install("mypy")
    session.install("types-attrs")
    session.install("types-requests")
    session.run("mypy", "zenora")


@nox.session(reuse_venv=True)
def formatting(session):
    session.install("black")
    session.run("black", "./")


@nox.session(reuse_venv=True)
def lint(session):
    session.install("flake8")
    session.run(
        "flake8",
        "--statistics",
        "--show-source",
        "--benchmark",
        "--tee",
    )


@nox.session(reuse_venv=True)
def docs(session):
    session.install("attrs")
    session.install("requests")
    session.install("pdoc3")

    session.run("pdoc", "--html", "zenora", "--force", external=True)
