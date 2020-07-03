# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import subprocess
import sphinx
import packaging.version
from markdown_code_symlinks import LinkParser, MarkdownSymlinksDomain

# -- Project information -----------------------------------------------------

project = 'Markdown Symlinks Tests'
copyright = '2020, SymbiFlow Authors'
author = 'SymbiFlow Authors'

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

master_doc = 'index'

sphinx_v3_0 = packaging.version.parse("3.0.0")
sphinx_v = packaging.version.parse(sphinx.__version__)

if sphinx_v >= sphinx_v3_0:
    extensions = ['recommonmark']
else:
    extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Tests --------------------------------------------------------------------

if "TEST" in os.environ:
    all_files = [f for f in os.listdir() if os.path.isfile(f)]
    test_name = os.environ["TEST"]

    if test_name == 'int_link_test':
        master_doc = 'int_link_test'
        used_files = ['int_link_test.md']
    elif test_name == 'ext_link_test':
        master_doc = 'ext_link_test'
        used_files = [
            'ext_link_test.md',
            'int_file.md'
        ]
    else:
        assert False, "Unsupported test name"

    exclude_patterns = [x for x in all_files if x not in used_files]

# -- Print Used Python Packages -----------------------------------------------

subprocess.run("pip3 list --format=columns", shell=True)
print("----------------------------------------------------------\n")

# -- Markdown Symlinks Setup --------------------------------------------------

source_parsers = {
    '.md': 'markdown_code_symlinks.LinkParser',
}

source_suffix = ['.rst', '.md']


def setup(app):
    github_code_branch = 'blob/fix_links/'
    github_code_repo = 'https://github.com/SymbiFlow/sphinxcontrib-markdown-symlinks/'

    docs_root_dir = os.path.realpath(os.path.dirname(__file__))
    code_root_dir = os.path.realpath(os.path.join(docs_root_dir, "..", ".."))

    MarkdownSymlinksDomain.init_domain(
        github_code_repo, github_code_branch, docs_root_dir, code_root_dir)
    MarkdownSymlinksDomain.find_links()
    app.add_domain(MarkdownSymlinksDomain)
    app.add_config_value(
        'recommonmark_config', {
            'github_code_repo': github_code_repo,
        }, True)
