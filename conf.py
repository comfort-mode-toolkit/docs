# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Comfort Mode Toolkit'
copyright = '2025, Lalitha A R'
author = 'Lalitha A R'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cm-colors')))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon', # Recommended if you use Google or NumPy style docstrings
    'sphinx.ext.viewcode',
    'myst_parser',  # For Markdown support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

html_theme_options = {
    'sidebar_bg': '#ECEAF3',
    'body_text': '#1A1A1A',
    'sidebar_text': '#1A1A1A',
    'sidebar_link': '#14407C',
    'link': '#14407C',
    'anchor': '#232259',
    # add other alabaster options as needed
}