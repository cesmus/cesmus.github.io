#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cesmus'
SITENAME = 'Cesmus'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SIDEBAR_NAME = 'Cesmus'
SIDEBAR_SUBNAME = 'data | software | computer networks | sysadmin'
#SIDEBAR_EMAIL = '<i>firstname</i>.<i>lastname</i>@gmail.com'
SIDEBAR_LOCATION = 'Colombia'
SIDEBAR_TAGS = ['linux',
                'python',
                'data',
                'web',
                ]

DEFAULT_DATE = 'fs'
WITH_FUTURE_DATES = True
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
STATIC_PATHS = ['images', 'pdfs', 'widgets', 'extra']
PAGE_EXCLUDES = ['widgets', '.ipynb_checkpoints']
ARTICLE_EXCLUDES = ['widgets', '.ipynb_checkpoints']
EXTRA_PATH_METADATA = {
    'images/favicon.png': {'path': 'favicon.png'},
    #'extra/CNAME': {'path': 'CNAME'},
}
THEME = 'themes/pure'
MD_EXTENSIONS = [
                 #'codehilite(css_class=highlight,'
                 #'guess_lang=False,linenums=False)',
                 #'headerid',
                 #'extra'
                 ]
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
PLUGIN_PATHS = ['pelican-plugins', 'plugins']
PLUGINS = [
           #'render_math',
           #'summary',
           #'neighbors',
           #'pdf',
           ]
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DIRECT_TEMPLATES = ('index', 'archives')
ARCHIVES_SAVE_AS = 'archives/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
TWITTER_USERNAME = ''
GITHUB_USERNAME = 'cesmus'
LINKEDIN_USERNAME = ''
STATCOUNTER = ''
DISQUS_SITENAME = 'cesmus'
MENUITEMS = [('Home', '/'),
             ('Projects', '/projects/'),
             #('Books', '/books/'),
             ('About', '/about/'),
             ]
DATE_FORMATS = {
    'en': '%Y-%m-%d',
}
