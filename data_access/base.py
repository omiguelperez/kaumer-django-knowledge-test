# -*- coding: utf-8 -*-

from django.db import models
from uuid import uuid4, UUID


class DomainModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not isinstance(self.id, UUID):
            self.id = uuid4()
        super(DomainModel, self).save(*args, **kwargs)
