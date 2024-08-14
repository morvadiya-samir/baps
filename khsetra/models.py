from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from mandir.models import Mandir

class BaseModel(TimeStampedModel):
    ACTIVE = 0
    DELETED = 1

    STATUS = (
        (ACTIVE, _('Active')),
        (DELETED, _('Deleted')),
    )
    status = models.IntegerField(_("The life cycle status of this object"), choices=STATUS, blank=True, null=True,default=ACTIVE)

class Khsetra(BaseModel):
    name = models.CharField(_("Name of Khsetra"), max_length=1024, blank=True, null=True)
    number = models.CharField(_("Unique number of Khsetra"), max_length=64, blank=True, null=True)
    mandir = models.ForeignKey(Mandir, on_delete=models.CASCADE,blank=True, null=True)
    nirdeshak_name = models.CharField(_("Name of Nirdeshak"), max_length=1024, blank=True, null=True)
    nirdeshak_contact_number = models.CharField(_("Contact number of Nirdeshak"), max_length=16, blank=True, null=True)
    sanyojak_name = models.CharField(_("Name of Sanyojak"), max_length=1024, blank=True, null=True)
    sanyojak_contact_number = models.CharField(_("Contact number of Sanyojak"), max_length=16, blank=True, null=True)