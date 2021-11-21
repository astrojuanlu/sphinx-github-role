from __future__ import annotations

from pathlib import Path

import pytest
from sphinx.errors import ExtensionError
from sphinx.testing.util import SphinxTestApp


@pytest.mark.parametrize(
    "",
    [
        pytest.param(marks=pytest.mark.sphinx),
        pytest.param(marks=pytest.mark.sphinx(testroot="myst")),
    ],
)
def test_github_role_produces_html_hyperlink(app: SphinxTestApp) -> None:
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


@pytest.mark.sphinx(testroot="malformed-link")
def test_malformed_link_raises_error(
    app: SphinxTestApp,
) -> None:
    with pytest.raises(ValueError, match="Malformed link"):
        app.build()


# Config is compatible with expected config (2-sequence)
# but type is incompatible, which raises a warning
@pytest.mark.sphinx(confoverrides={"github_default_org_project": "aa"})
def test_invalid_config_emits_warning(
    app: SphinxTestApp,
) -> None:
    app.build()
    assert app.statuscode != 0, "Expected build problem but it finished successfully"


def test_malformed_config_emits_warning(tempdir, make_app):
    conf_contents = """github_default_org_project = None

extensions = [
    "sphinx_github_role",
]

nitpicky = True
"""
    (tempdir / "conf.py").write_text(conf_contents)
    with pytest.raises(
        ExtensionError, match="Invalid github_default_org_project configuration"
    ):
        make_app(srcdir=tempdir)


def test_missing_default_org_with_project_set_raises_error(tempdir, make_app):
    conf_contents = """github_default_org_project = (None, "proj")

extensions = [
    "sphinx_github_role",
]

nitpicky = True
"""
    (tempdir / "conf.py").write_text(conf_contents)
    with pytest.raises(
        ExtensionError,
        match="GitHub default organization cannot be empty if default project is set",
    ):
        make_app(srcdir=tempdir)


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


@pytest.mark.sphinx(testroot="custom-link-text")
def test_github_role_custom_link_text_produces_html_hyperlink(
    app: SphinxTestApp,
) -> None:
    expected_chunk = (
        '<a class="reference external" '
        'href="https://github.com/readthedocs/readthedocs.org/issues/1">'
        "Issue #1</a>"
    )

    app.build()
    assert app.statuscode == 0, "Build finished with problems"

    path = Path(app.outdir) / "index.html"
    assert path.exists()

    content = open(path).read()

    assert expected_chunk in content
