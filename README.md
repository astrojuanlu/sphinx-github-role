# sphinx-github-role

A github role for Sphinx

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
