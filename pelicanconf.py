#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

FIRST_NAME = 'Jezeniel'
LAST_NAME = 'Zapanta'
AUTHOR = f'{FIRST_NAME}  {LAST_NAME}'
AUTHOR_IMG = 'images/author.jpg'
SITENAME = 'Jezeniel Zapanta'
SITEURL = ''
SITE_DESCRIPTION="This is my personal website. I blog about software development, tools that I use or just about anything."

GITHUB_URL = 'https://github.com/jezeniel'
TWITTER_URL = 'https://twitter.com/jezeniel'
EMAIL_URL = 'mailto:jezeniel.zapanta@gmail.com'

NAVBAR = [
    ('About', 'about/'), ('Blog', 'blog/'), ('Projects', 'projects/')
]

THEME = 'themes/end2end'

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = 'en'

DIRECT_TEMPLATES = ['index']
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''

## Markdown
MARKDOWN = {
    'extensions': [
        'markdown.extensions.smarty',
        'markdown.extensions.extra',
        'markdown3_newtab',
    ]
}

## Custom URLS

# Article
ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{slug}/index.html'

# Category 
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

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

IGNORE_FILES = ['.#*', '*.sass', '*.scss', '_sass', '.sass-cache']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
