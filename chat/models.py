# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models



class Chat(models.Model):
    chat_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
