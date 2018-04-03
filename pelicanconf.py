#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Julien Lebranchu'
SITENAME = 'Observatoire des Ecosystèmes Pélagiques Tropicaux exploités'
SITEURL = ''

STATIC_PATHS = ['images', 'pdfs']

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/fr']
ARTICLE_PATHS = ['blog/fr']

# plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites','always_modified','tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('UMR 248 MARBEC', 'http://www.umr-marbec.fr','/images/logo_marbec_h75.png'),
         ('FEAMP', 'http://www.europe-en-france.gouv.fr/L-Europe-s-engage/Fonds-europeens-2014-2020/Politique-de-la-peche-et-des-affaires-maritimes/FEAMP','/images/logo_feamp.png'),
         ('Institut de Recherche pour le Développement', 'https://www.ird.fr', '/images/logo_ird_h75.png'),
)

FOOTER_ITEMS=[]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme and theme localization
THEME = '../pelican-fh5co-ob7'
I18N_GETTEXT_LOCALEDIR = '../pelican-fh5co-ob7/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'fr_FR'
DEFAULT_LANG = 'fr'
LOCALE = 'fr_FR'

# i18n
# I18N_SUBSITES = {
#   'en': {
#     'PAGE_PATHS': ['pages/en'],
#     'ARTICLE_PATHS': ['blog/en'],
#     'LOCALE': 'en_UK'
#   }
# }

# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.svg'

# special content
HERO = [
  # {
  #   'image': '/images/hero/background-1.jpg',
  #   # for multilanguage support, create a simple dict
  #   'title': {
  #     'en':'Some special content',
  #     'fr': 'Spezieller Inhalt'
  #   },
  #   'text': {
  #     'fr': 'Any special content you want to tease here',
  #     'de': 'Jeglicher spezieller Inhalt den Sie hier bewerben möchten'
  #   },
  #   'links': [
  #     {
  #       'icon': 'icon-code',
  #       'url': 'https://github.com/claudio-walser/pelican-fh5co-marble',
  #       'text': 'Github'
  #     }
  #   ]
  # },
  {
    'image': '/images/hero/background-1.jpg',
    # keep it a string if you dont need multiple languages
    'title': {'fr': '', 'en': ''},
    # keep it a string if you dont need multiple languages
    'text': {'fr': '', 'en': ''},
    'links': []
  },
  {
    'image': '/images/hero/background-2.jpg',
    # keep it a string if you dont need multiple languages
    'title': {'fr':'','en':''},
    # keep it a string if you dont need multiple languages
    'text': {'fr':'','en':''},
    'links': []
  },
  {
    'image': '/images/hero/background-3.jpg',
    # keep it a string if you dont need multiple languages
    'title': {'fr':'','en':''},
    # keep it a string if you dont need multiple languages
    'text': {'fr':'','en':''},
    'links': []
  },
  {
    'image': '/images/hero/background-4.jpg',
    # keep it a string if you dont need multiple languages
    'title': {'fr':'','en':''},
    # keep it a string if you dont need multiple languages
    'text': {'fr':'','en':''},
    'links': []
  },
  {
    'image': '/images/hero/background-5.jpg',
    # keep it a string if you dont need multiple languages
    'title': {'fr':'','en':''},
    # keep it a string if you dont need multiple languages
    'text': {'fr':'','en':''},
    'links': []
  },
  {
    'image': '/images/hero/background-6.jpg',
    # keep it a string if you dont need multiple languages
    'title': {'fr':'','en':''},
    # keep it a string if you dont need multiple languages
    'text': {'fr':'','en':''},
    'links': []
  },
  {
    'image': '/images/hero/background-7.jpg',
    # keep it a string if you dont need multiple languages
    'title': {'fr':'','en':''},
    # keep it a string if you dont need multiple languages
    'text': {'fr':'','en':''},
    'links': []
  },
  {
    'image': '/images/hero/background-8.jpg',
    # keep it a string if you dont need multiple languages
    'title': {'fr':'','en':''},
    # keep it a string if you dont need multiple languages
    'text': {'fr':'','en':''},
    'links': []
  }
]


# Social widget
SOCIAL = ()
#(
# ('Github', 'https://www.github.com/claudio-walser'),
#  ('Facebook', 'https://www.facebook.com'),
#  ('Twitter', 'https://www.twitter.com'),
#  ('Google+', 'https://plus.google.com')
#)


ABOUT = {
  'image': '/images/about/objectif.png',
  'mail': 'ob7@ird.fr',
  # keep it a string if you dont need multiple languages
  'text': 'Avenue Jean Monnet,<br/> CS 30171, 34203 Sète cedex, <br/>France',
  #'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Avenue Jean Monnet,<br/> CS 30171, 34203 Sète cedex, <br/>France ',
  'phone': '+33(0) 4 99 57 32 00'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
#  ('Archive', 'archives.html'),
#  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]

# setup disqus
DISQUS_SHORTNAME = ''
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# setup google maps
#GOOGLE_MAPS_KEY = ''
