# -*- coding: utf-8 -*-


import sys
import os

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

source_suffix = '.rst'
master_doc = 'index'
project = u'Test index'
copyright = u'2019, Test'
author = u'Test'
version = '1'
release = '1'
language = 'ru'
exclude_patterns = []
highlight_language = 'c#'
pygments_style = 'vs'
todo_include_todos = False
html_show_sphinx = False
html_search_language = 'en'
htmlhelp_basename = 'TestIndex'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}
latex_documents = [
  (master_doc, 'TestIndex.tex', u'TestIndex', author, 'manual'),
]

man_pages = [
    (master_doc, 'TestIndex', u'TestIndex', [author], 1)
]

texinfo_documents = [
  (master_doc, 'TestIndex', u'TestIndex', author, 'TestIndex', 'One line description of project.', 'Miscellaneous'),
]

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']

intersphinx_mapping = {'https://docs.python.org/': None}
