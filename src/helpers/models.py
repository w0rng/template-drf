from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UUIDModel(models.Model):
    id = models.UUIDField(_('ID'), default=uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True
