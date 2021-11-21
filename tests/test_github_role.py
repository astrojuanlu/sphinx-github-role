from __future__ import annotations

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
    expected_chunk = (
        '<a class="reference external" '
        'href="https://github.com/readthedocs/readthedocs.org/issues/1">'
        "readthedocs/readthedocs.org#1</a>"
    )

    app.build()
    assert app.statuscode == 0, "Build finished with problems"

    path = Path(app.outdir) / "index.html"
    assert path.exists()

    content = open(path).read()

    assert expected_chunk in content


# Config is compatible with expected config (2-sequence)
# but type is incompatible, which raises a warning
@pytest.mark.sphinx(confoverrides={"github_default_org_project": "aa"})
def test_invalid_config_emits_warning(
    app: SphinxTestApp,
) -> None:
    app.build()
    assert app.statuscode != 0, "Expected build problem but it finished successfully"


# test fails at the initialization stage, find some other way
# @pytest.mark.sphinx(confoverrides={"github_default_org_project": None})
# def test_invalid_config_emits_warning(
#     app: SphinxTestApp,
#     chunks: list[str],
# ) -> None:
#     app.build()
#     assert app.statuscode != 0, "Expected build problem but it finished successfully"


# test fails at the initialization stage, find some other way
# @pytest.mark.sphinx(confoverrides={"github_default_org_project": (None, "proj")})
# def test_missing_default_org_with_project_set_raises_error(
#     app: SphinxTestApp,
#     chunks: list[str],
# ) -> None:
#     app.build()
#     assert app.statuscode != 0, "Expected build problem but it finished successfully"


@pytest.mark.sphinx(testroot="default-org")
def test_default_org_produces_html_hyperlink(
    app: SphinxTestApp,
) -> None:
    expected_chunk = (
        '<a class="reference external" '
        'href="https://github.com/readthedocs/readthedocs.org/issues/1">'
        "readthedocs.org#1</a>"
    )

    app.build()
    assert app.statuscode == 0, "Build finished with problems"

    path = Path(app.outdir) / "index.html"
    assert path.exists()

    content = open(path).read()

    assert expected_chunk in content


@pytest.mark.sphinx(testroot="default-project")
def test_default_org_and_project_produces_html_hyperlink(
    app: SphinxTestApp,
) -> None:
    expected_chunk = (
        '<a class="reference external" '
        'href="https://github.com/readthedocs/readthedocs.org/issues/1">'
        "#1</a>"
    )

    app.build()
    assert app.statuscode == 0, "Build finished with problems"

    path = Path(app.outdir) / "index.html"
    assert path.exists()

    content = open(path).read()

    assert expected_chunk in content


@pytest.mark.sphinx(testroot="default-project-no-conf")
def test_incomplete_link_raises_error(
    app: SphinxTestApp,
) -> None:
    with pytest.raises(
        ValueError, match="Incomplete configuration or GitHub reference"
    ):
        app.build()
