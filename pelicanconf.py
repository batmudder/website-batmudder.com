#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'batmudder'
SITENAME = 'batmudder.com'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'public'
ARTICLE_PATHS = [ 'posts' ]
PAGE_PATHS = [ 'pages' ]
STATIC_PATHS = [ 'images', 'static' ]
IGNORE_FILES = [ '.#*', '_template*.md' ]
INDEX_SAVE_AS = 'blog_index.html'
#THEME = 'themes/themename'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARCHIVES_SAVE_AS = 'posts/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'

AUTHOR_SAVE_AS = ''

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d %Y'

MENUITEMS = [
        ('Home', '/'),
        ('Blog', '/blog_index.html'),
]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
