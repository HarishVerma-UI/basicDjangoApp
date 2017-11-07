# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Movie ,Song ,Singer

admin.site.register(Movie)
admin.site.register(Song)
admin.site.register(Singer)


# Register your models here.
