#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jezeniel Zapanta'
AUTHOR_IMG = 'images/author.jpg'
SITENAME = 'jezeniel'
SITEURL = ''

GITHUB_URL = 'https://github.com/jezeniel'
TWITTER_URL = 'https://twitter.com/jezeniel'
EMAIL_URL = 'mailto:jezeniel.zapanta@gmail.com'

NAVBAR = [('pages/about/', 'About'), ('#', 'Blog'), ('#', 'Projects')]

THEME = 'themes/end2end'

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

IGNORE_FILES = ['.#*', '*.sass', '*.scss', '_sass']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
