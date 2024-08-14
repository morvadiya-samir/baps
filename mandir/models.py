from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

class BaseModel(TimeStampedModel):
    ACTIVE = 0
    DELETED = 1

    STATUS = (
        (ACTIVE, _('Active')),
        (DELETED, _('Deleted')),
    )
    status = models.IntegerField(_("The life cycle status of this object"), choices=STATUS, blank=True, null=True,
                                 default=ACTIVE)

    class Meta:
        abstract = True

class Mandir(BaseModel):
    name = models.CharField(_("Name of Mandir"), max_length=1024, blank=True, null=True)
    city = models.CharField(_("City of Mandir"), max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return "Name: " + str(self.name) + " City: " + str(self.city)