# Sphinx Contrib - Markdown Symlinks

This small Python file enables you to create a symbolic link to markdown pages
outside your docs directory and have links still work. This is useful if you
have things like the
[`CONTRIBUTING.md`](https://blog.github.com/2012-09-17-contributing-guidelines/)
or
[`CODE_OF_CONDUCT.md`](https://blog.github.com/2012-09-17-contributing-guidelines/)
in your repository that you also want to appear in your Sphinx documentation.

As the Markdown documents will have links relative to the source code root,
rather than the place they are now linked too, this code will fixes these paths
up.

The code also makes relative links between two Markdown documents found inside
the Sphinx documentation work even if there relative positions are now totally
different.

# Install

You can install it either via;
```shell
pip install -e "git+https://github.com/SymbiFlow/sphinxcontrib-markdown-symlinks"
```

Or add the following to your `requirements.txt`
```
-e git+https://github.com/SymbiFlow/sphinxcontrib-markdown-symlinks
```

# Set Up

```python

# Add Markdown support by following the recommonmark install instructions.
# https://recommonmark.readthedocs.io/en/latest/#getting-started

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': 'markdown_code_symlinks.LinkParser',
}

source_suffix = ['.rst', '.md']

# Replace ;
from markdown_links import MarkdownLinks
def setup(app):
    github_code_repo = 'https://github.com/repo/link'
    github_code_branch = 'blob/your/branch'

    docs_root_dir = os.path.realpath(os.path.dirname(__file__))
    # Create code root dir relative to docs_root_dir
    code_root_dir = os.path.realpath(os.path.join(docs_root_dir, "..", ".."))

    MarkdownSymlinksDomain.init_domain(
        github_code_repo, github_code_branch, docs_root_dir, code_root_dir)
    MarkdownSymlinksDomain.find_links()
    app.add_domain(MarkdownSymlinksDomain)
    app.add_config_value(
        'recommonmark_config', {
            'github_code_repo': github_code_repo,
        }, True)
```

When running, the build should output something like the following now;
```
{'code2docs': {'BUILDING.md': 'sth/build_sth.md',
               'CONTRIBUTING.md': 'sth/dev/guidelines.md',
               'README.developers.md': 'sth/dev/index.md'},
 'docs2code': {'sth/build_sth.md': 'BUILDING.md',
               'sth/dev/guidelines.md': 'CONTRIBUTING.md',
               'sth/dev/index.md': 'README.developers.md'}}
```

# License

This extension is available under your choice of;

 * [ISC License](COPYING) ([see also](https://creativecommons.org/publicdomain/zero/1.0/legalcode))
