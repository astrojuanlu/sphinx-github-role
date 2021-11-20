# See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-573092764
from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp


# TODO: Is there any way to parametrize a custom mark?
# For example, repeat this test with
# @pytest.mark.sphinx(testroot="root") and
# @pytest.mark.sphinx(testroot="myst")
def test(app: SphinxTestApp) -> None:
    # app is a Sphinx application object for default sphinx project
    # (tests/cases/test-root)

    # See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-974680232
    app.warningiserror = app.keep_going = True

    app.build()

    path = Path(app.outdir) / "index.html"
    assert path.exists()

    content = open(path).read()

    chunks = [
        (
            '<a class="reference external" '
            'href="https://github.com/readthedocs/readthedocs.org/issues/1">'
            "readthedocs/readthedocs.org#1</a>"
        ),
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(testroot="myst")
def test_myst(app: SphinxTestApp) -> None:
    # app is a Sphinx application for myst sphinx project
    # (tests/cases/test-myst)
    app.warningiserror = app.keep_going = True

    app.build()

    path = Path(app.outdir) / "index.html"
    assert path.exists()

    content = open(path).read()

    chunks = [
        (
            '<a class="reference external" '
            'href="https://github.com/readthedocs/readthedocs.org/issues/1">'
            "readthedocs/readthedocs.org#1</a>"
        ),
    ]

    for chunk in chunks:
        assert chunk in content
