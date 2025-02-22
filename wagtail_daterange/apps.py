# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RangeFilterConfig(AppConfig):
    name = 'wagtail_daterange'
    verbose_name = _('Wagtail Date Range Filter')
