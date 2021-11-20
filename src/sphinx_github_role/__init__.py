"""
sphinx-github-role

A github role for Sphinx
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from docutils import nodes
from sphinx.util.docutils import ReferenceRole

if TYPE_CHECKING:
    from docutils.nodes import Node, system_message
    from sphinx.application import Sphinx

__version__ = "0.1"


class GitHub(ReferenceRole):
    def run(self) -> tuple[list[Node], list[system_message]]:
        paragraph_node = nodes.paragraph(text="GitHub!")
        return [paragraph_node], []


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_role("github", GitHub())

    return {"version": __version__, "parallel_read_safe": True}
