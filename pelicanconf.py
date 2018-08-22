#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Zack Soliman'
SITENAME = 'Exponential Divergence'
SITEURL = ''

PATH = 'content'
THEME = 'themes/voce'
PLUGIN_PATHS = os.path.join(THEME, "plugins")
TIMEZONE = 'America/Montreal'

TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'

DEFAULT_LANG = 'en'
FUZZY_DATES = True

PLUGINS = ["assets"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

MANGLE_EMAILS = True
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS_ID = None
GOOGLE_ANALYTICS_PROP = None

GLOBAL_KEYWORDS = ["data science",
                   "machine learning",
                   "deep learning",
                   "programming",
                   "coding",
                   "python",
                   "lisp",
                   "clojure",
                   "hacking",
                   "computer science",
                   "math",
                   "mathematics"]
