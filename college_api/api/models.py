from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class College(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    attributes = models.ManyToManyField(Attribute)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
