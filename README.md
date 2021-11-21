# sphinx-github-role

[![Documentation Status](https://readthedocs.org/projects/sphinx-github-role/badge/?version=latest)](https://sphinx-github-role.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A github role for Sphinx.

## Usage

MyST:

```md
# index.md
See {github}`astrojuanlu/sphinx-github-role#1`.
```

reStructuredText:

```rst
# index.rst
See :github:`astrojuanlu/sphinx-github-role#1`.
```

The extension accepts a configuration `github_default_org_project`
that can be a tuple `("default_org", "default_project")`
to save some typing. For example, with this configuration:

```python
# conf.py
github_default_org_project = ("astrojuanlu", None)
```

you can type this:

```md
# index.md
See {github}`sphinx-github-role#1`.
```

and with this configuration:

```python
# conf.py
github_default_org_project = ("astrojuanlu", "sphinx-github-role")
```

you only need to type this:

```md
# index.md
See {github}`#1`.
```

## Contribute

Feel free to open an issue to report problems or suggest new features!
