# See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-573092764
import pytest
from sphinx.testing.util import SphinxTestApp


def test(app: SphinxTestApp) -> None:
    # app is a Sphinx application object for default sphinx project
    # (tests/cases/test-root)

    # See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-974680232
    app.warningiserror = app.keep_going = True

    app.build()


@pytest.mark.sphinx(testroot="myst")
def test_myst(app: SphinxTestApp) -> None:
    # app is a Sphinx application for myst sphinx project
    # (tests/cases/test-myst)
    app.warningiserror = app.keep_going = True

    app.build()
