# See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-573092764
from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp


# TODO: Awaiting for a nicer way to do this,
# See https://stackoverflow.com/q/70053419/554319
@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, marks=pytest.mark.sphinx),
        pytest.param(None, marks=pytest.mark.sphinx(testroot="myst")),
    ],
)
def test_github_role_produces_html_hyperlink(app: SphinxTestApp, _: None) -> None:
    # app is a Sphinx application object for default sphinx project
    # (tests/cases/test-root)
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
