"""
sphinx-github-role

A github role for Sphinx
"""
from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

from docutils import nodes
from sphinx.util.docutils import SphinxRole

if TYPE_CHECKING:
    from docutils.nodes import Node, system_message
    from sphinx.application import Sphinx

__version__ = "0.1"


class GitHub(SphinxRole):
    # For example: org/proj#1
    gh_re = re.compile(r"(?P<org>.+)/(?P<proj>.+)#(?P<num>\d+)")
    # The /issues/{num} and /pull/{num} URLs automatically redirect
    gh_tpl = "https://github.com/{org}/{proj}/issues/{num}"

    def run(self) -> tuple[list[Node], list[system_message]]:
        # breakpoint()
        match = self.gh_re.fullmatch(self.text)
        node = nodes.reference(
            self.rawtext,
            self.text,
            refuri=self.gh_tpl.format(**match.groupdict()),
        )

        return [node], []


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_role("github", GitHub())

    return {"version": __version__, "parallel_read_safe": True}
