from __future__ import unicode_literals
from model_utils import Choices
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_extensions.db.models import TimeStampedModel
# from audit_log.models import AuthStampedModel
from .managers import *
from .constants import FileConstants, HaribhaktConstants, MandalConstants
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# from dataio import DataIOProvider/
from mandir.models import Mandir
from khsetra.models import Khsetra
from mandal.models import Mandal


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


class File(BaseModel, FileConstants):
    file = models.FileField()
    type = models.IntegerField(_("type"), choices=FileConstants.TYPES)

    process_stats = models.IntegerField(_("File Process stats"), choices=FileConstants.PROCESS_STATUS,
                                        default=FileConstants.PROCESS_STATUS_PENDING)

    objects = FileManager()

    def __unicode__(self):
        return "{} ({})".format(self.file, self.type)

    def is_type_haribhakto(self):
        return self.type == self.FILE_TYPE_HARIBHAKTO

    def mark_file_process_as_success(self):
        # set file upload status as Success
        self.process_stats = FileConstants.PROCESS_STATUS_SUCCESS
        self.save()

    def mark_file_process_as_failure(self):
        # set file upload status as Success
        self.process_stats = FileConstants.PROCESS_STATUS_FAILED
        self.save()

    def get_file_data(self):
        """
        This is a model method which will read self.file and return the json of that file
        :return: list of dict of  data of the file being read
        """
        data = DataIOProvider.get_data_handler(self.file.path)
        return data.list()

    def has_valid_headers(self):
        """
        :return: whether the headers passed are valid as per the file type object.
        """
        uploaded_file_headers = self.get_csv_file_headers()
        required_header_list = []
        if self.is_type_haribhakto():
            required_header_list = FileConstants.HARIBHAKTO_FILE_HEADERS
        for header in required_header_list:
            if not header in (single_header for single_header in uploaded_file_headers):
                return False

        return True

    def get_csv_file_headers(self):
        """

        :return: return the Headers of CSV file
        """
        data = DataIOProvider.get_data_handler(self.file.path)
        return data.get_headers()


# class Mandir(BaseModel):
#     name = models.CharField(_("Name of Mandir"), max_length=1024, blank=True, null=True)
#     city = models.CharField(_("City of Mandir"), max_length=1024, blank=True, null=True)

#     def __unicode__(self):
#         return "Name: " + str(self.name) + " City: " + str(self.city)


# class Khsetra(BaseModel):
#     name = models.CharField(_("Name of Khsetra"), max_length=1024, blank=True, null=True)
#     number = models.CharField(_("Unique number of Khsetra"), max_length=64, blank=True, null=True)
#     mandir = models.ForeignKey(Mandir, on_delete=models.CASCADE,blank=True, null=True)
#     nirdeshak_name = models.CharField(_("Name of Nirdeshak"), max_length=1024, blank=True, null=True)
#     nirdeshak_contact_number = models.CharField(_("Contact number of Nirdeshak"), max_length=16, blank=True, null=True)
#     sanyojak_name = models.CharField(_("Name of Sanyojak"), max_length=1024, blank=True, null=True)
#     sanyojak_contact_number = models.CharField(_("Contact number of Sanyojak"), max_length=16, blank=True, null=True)


# class Mandal(BaseModel):
#     name = models.CharField(_("Name of Mandal"), max_length=1024, blank=True, null=True)
#     number = models.CharField(_("Unique number of Mandal"), max_length=64, blank=True, null=True)
#     type = models.CharField(_("Mandal type"), choices=MandalConstants.MANDAL_TYPE_CHOICES, max_length=16)
#     khestra = models.ForeignKey(Khsetra, on_delete=models.CASCADE,blank=True, null=True)
#     sanchaalak_name = models.CharField(_("Name of Mandal Sanchalak"), max_length=1024, blank=True, null=True)
#     sanchaalak_contact_number = models.CharField(_("Contact number of Mandal Sanchalak"), max_length=16, blank=True,
#                                                  null=True)
#     nirikshak_name = models.CharField(_("Name of Nirikshak"), max_length=1024, blank=True, null=True)
#     nirikshak_contact_number = models.CharField(_("Contact number of Nirikshak"), max_length=16, blank=True, null=True)


class Haribhakt(BaseModel):
    name = models.CharField(_("Name of Haribhakt"), max_length=1024, blank=True, null=True)
    is_gunbhavi = models.BooleanField(_("Is Haribakt gunbhavi or not ?"), default=False)
    gender = models.CharField(_("Gender"), choices=HaribhaktConstants.GENDER_CHOICES, max_length=16)
    is_head_of_family = models.BooleanField(_("Is Haribakt Head of Family ?"), default=False)
    relation_with_hof = models.CharField(_("Relation with Head of Family"), max_length=1024, blank=True, null=True)
    head_of_family = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True)
    contact_number_1 = models.CharField(_("Contact number 1"), max_length=10, blank=True, null=True)
    contact_number_2 = models.CharField(_("Contact number 2"), max_length=10, blank=True, null=True)
    contact_number_3 = models.CharField(_("Contact number 3"), max_length=10, blank=True, null=True)
    birth_date = models.DateField(_("Date of Birth"), blank=True, null=True)
    number_of_years_of_satsang = models.SmallIntegerField(_("Number of years of satsang"), blank=True, null=True)

    nitya_pooja = models.BooleanField(_("Nitya Pooja ?"), default=True)
    tilak_chaandlo = models.BooleanField(_("Tilak Chaandlo ?"), default=True)
    vyasan = models.BooleanField(_("Vyasan ?"), default=False)
    vyasan_type = models.CharField(_("Type of vyasan"), max_length=1024, blank=True, null=True)

    onion_garlic = models.BooleanField(_("Onion and Garlic ?"), default=False)
    weekly_sabha = models.BooleanField(_("Weekly Sabha ?"), default=True)
    poonam_sabha = models.BooleanField(_("Poonam Pooja ?"), default=False)
    ghar_sabha = models.BooleanField(_("Ghar Sabha ?"), default=True)
    vachnamrut_swami_ni_vaato_vanchan = models.BooleanField(_("Vachnamrut Swami ni vaato nu Vaanchan ?"), default=True)
    satsang_sikshan_pariksha = models.BooleanField(_("Satsang Sikshan Pariksha ?"), default=True)
    monthtly_donation = models.IntegerField(_("Monthly Donation ?"), blank=True, null=True)

    file = models.ForeignKey(File, on_delete=models.CASCADE,blank=True, null=True)
    mandal = models.ForeignKey(Mandal, on_delete=models.CASCADE,blank=True, null=True)
    objects = HaribhaktManager()

    def __unicode__(self):
        # Number: 9854815789, Call Text: lhvhslvhlvsv, SMS Text: jhdvjkdhvkdj, Outcomes Type: 1/2/3
        return "ID: " + str(self.id) + " Name : " + self.name
