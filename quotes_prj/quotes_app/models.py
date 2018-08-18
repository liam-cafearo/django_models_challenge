# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Quote(models.Model):

    class Meta:  # included this to ensure build in IDE
        app_label = "quotes_app"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
