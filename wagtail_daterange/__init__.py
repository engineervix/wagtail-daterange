# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django 


__author__ = 'Michael Yin'
__version__ = '0.1.2'


if django.VERSION < (3, 2):
    default_app_config = 'wagtail_daterange.apps.RangeFilterConfig'

VERSION = __version__
