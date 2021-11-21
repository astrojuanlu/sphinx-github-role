from __future__ import annotations

from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.fixture
def chunks():
    return [
        (
            '<a class="reference external" '
            'href="https://github.com/readthedocs/readthedocs.org/issues/1">'
            "readthedocs/readthedocs.org#1</a>"
        ),
    ]


# TODO: Awaiting for a nicer way to do this,
# See https://stackoverflow.com/q/70053419/554319
@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, marks=pytest.mark.sphinx),
        pytest.param(None, marks=pytest.mark.sphinx(testroot="myst")),
    ],
)
def test_github_role_produces_html_hyperlink(
    app: SphinxTestApp, chunks: list[str], _: None
) -> None:
    app.build()

    path = Path(app.outdir) / "index.html"
    assert path.exists()

    content = open(path).read()

    for chunk in chunks:
        assert chunk in content
