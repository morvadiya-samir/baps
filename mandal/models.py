from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from khsetra.models import Khsetra
from core.constants import MandalConstants



class BaseModel(TimeStampedModel):
    ACTIVE = 0
    DELETED = 1

    STATUS = (
        (ACTIVE, _('Active')),
        (DELETED, _('Deleted')),
    )
    status = models.IntegerField(_("The life cycle status of this object"), choices=STATUS, blank=True, null=True,default=ACTIVE)

class Mandal(BaseModel):
    name = models.CharField(_("Name of Mandal"), max_length=1024, blank=True, null=True)
    number = models.CharField(_("Unique number of Mandal"), max_length=64, blank=True, null=True)
    type = models.CharField(_("Mandal type"), choices=MandalConstants.MANDAL_TYPE_CHOICES, max_length=16)
    khestra = models.ForeignKey(Khsetra, on_delete=models.CASCADE,blank=True, null=True)
    sanchaalak_name = models.CharField(_("Name of Mandal Sanchalak"), max_length=1024, blank=True, null=True)
    sanchaalak_contact_number = models.CharField(_("Contact number of Mandal Sanchalak"), max_length=16, blank=True,
                                                 null=True)
    nirikshak_name = models.CharField(_("Name of Nirikshak"), max_length=1024, blank=True, null=True)
    nirikshak_contact_number = models.CharField(_("Contact number of Nirikshak"), max_length=16, blank=True, null=True)