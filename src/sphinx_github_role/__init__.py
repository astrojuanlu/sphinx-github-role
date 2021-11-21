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
    from sphinx.config import Config

__version__ = "0.1"

_DEFAULTS = [None, None]


def setup_github_role(_: Sphinx, config: Config) -> None:
    if "github_default_org_project" in config.values:
        default_organization, default_project = config["github_default_org_project"]

        if not default_organization and default_project:
            raise ValueError(
                "GitHub default organization cannot be empty if default project is set"
            )

        _DEFAULTS[0] = default_organization
        _DEFAULTS[1] = default_project


class GitHub(SphinxRole):
    # For example: org/proj#1
    gh_re = re.compile(
        r"""((?P<org>.+)/)?  # Optional organization
        (?P<proj>.+)?  # Optional project
        \#(?P<num>\d+)  # Issue or pull request id""",
        re.VERBOSE,
    )
    # The /issues/{num} and /pull/{num} URLs automatically redirect
    gh_tpl = "https://github.com/{org}/{proj}/issues/{num}"

    def run(self) -> tuple[list[Node], list[system_message]]:
        # breakpoint()
        match = self.gh_re.fullmatch(self.text)

        parts = match.groupdict()
        parts["org"] = parts["org"] or _DEFAULTS[0]
        parts["proj"] = parts["proj"] or _DEFAULTS[1]
        if not parts["org"] or not parts["proj"]:
            raise ValueError(
                "Incomplete configuration or GitHub reference: "
                f"default organization = '{_DEFAULTS[0]}', "
                f"default project = '{_DEFAULTS[1]}', "
                f"role text = '{self.text}'"
            )

        node = nodes.reference(
            self.rawtext,
            self.text,
            refuri=self.gh_tpl.format(**parts),
        )

        return [node], []


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_config_value("github_default_org_project", ("", ""), None)
    app.add_role("github", GitHub())

    app.connect("config-inited", setup_github_role)

    return {"version": __version__, "parallel_read_safe": True}
