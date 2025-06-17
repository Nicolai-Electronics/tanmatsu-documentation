from __future__ import print_function, unicode_literals
import os
import os.path
import subprocess
import sys

sys.path.insert(0, os.path.abspath('.'))

from get_github_rev import get_github_rev

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tanmatsu'
copyright = '2025 Nicolai Electronics - CC-BY 4.0 license'
author = 'Nicolai Electronics'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_logo = "_static/tanmatsu.png"

html_theme_options = {
    'logo_only': True,
    'style_external_links': False,
    'style_nav_header_background': 'white',
}

html_context = {
    'display_github': True,
    "github_user": "nicolai-electronics",
    "github_repo": "tanmatsu-documentation",
    'github_version': "main",
    'github_url': "https://github.com/Nicolai-Electronics/tanmatsu-documentation",
    "conf_py_path": "/src/"
}

html_css_files = [
        'theme_overrides.css'
]
