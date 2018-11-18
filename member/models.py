# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'用户信息'

    def __unicode__(self):
        return self.user.username

