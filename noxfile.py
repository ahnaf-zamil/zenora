import nox


@nox.session(reuse_venv=True)
def tests(session):
    session.install("pytest")
    session.install("attrs")
    session.install("requests")
    session.run("pytest")


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
