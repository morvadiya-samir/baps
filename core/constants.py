from django.utils.translation import gettext_lazy as _
from model_utils import Choices


class FileConstants(object):
    """

    """
    # Raw Data Headers
    NAME = 'Name'
    IS_GUNBHAVI = 'Is Gunbhavi ?'
    GENDER = 'Gender'
    IS_HOF = 'Is Head of Family ?'
    RELATION_WITH_HOF = 'Relation with Head of Family'
    HOF = 'Head of the Family'
    CONTACT_NUM1 = 'Contact Number 1'
    CONTACT_NUM2 = 'Contact Number 2'
    CONTACT_NUM3 = 'Contact Number 3'
    DOB = 'Date Of Birth'
    SATSANG_DURATION = 'Satsant Duration (in years)'
    NITYA_PUJA = 'Nitya Puja ?'
    TILAK_CHAANDLO = 'Tilak Chaandlo ?'
    VYASAN = 'Vyasan ?'
    VYASAN_TYPE = 'Type of Vyasan ?'
    ONION_GARLIC = 'Onion Garlic ?'
    WEEKLY_SABHA = 'Weekly Sabha ?'
    POONAM_SABHA = 'Poonam Sabha ?'
    GHAR_SABHA = 'Ghar Sabha ?'
    VACHNAMURT_SWAMI_VAATO = 'Vachnamurt & Swami ni Vaato ?'
    SSP = 'SSP ?'
    MONTHLY_DONATION = 'Monthly Donation'

    HARIBHAKTO_FILE_HEADERS = [NAME, IS_GUNBHAVI, GENDER, IS_HOF, RELATION_WITH_HOF, HOF, CONTACT_NUM1, CONTACT_NUM2,
                               CONTACT_NUM3, DOB, SATSANG_DURATION, NITYA_PUJA, TILAK_CHAANDLO, VYASAN, VYASAN_TYPE,
                               ONION_GARLIC, WEEKLY_SABHA, POONAM_SABHA, GHAR_SABHA, VACHNAMURT_SWAMI_VAATO, SSP,
                               MONTHLY_DONATION]

    FILE_TYPE_HARIBHAKTO = 1

    # Type of files
    TYPES = Choices(
        (FILE_TYPE_HARIBHAKTO, 'haribhakto_details', _('haribhakto_details'))
    )

    FILE_TYPE_HEADER_MAP = {
        FILE_TYPE_HARIBHAKTO: HARIBHAKTO_FILE_HEADERS
    }

    PROCESS_STATUS_FAILED = 1
    PROCESS_STATUS_PENDING = 2
    PROCESS_STATUS_SUCCESS = 3
    PROCESS_STATUS = (
        (PROCESS_STATUS_FAILED, _('Failed')),
        (PROCESS_STATUS_PENDING, _('Pending')),
        (PROCESS_STATUS_SUCCESS, _('Success')),
    )


class MandalConstants(object):
    # Gender types
    BAL = "Bal"
    BALIKA = "Balika"
    YUVAK = "Yuvak"
    YUVATI = "Yuvati"
    SANYUKT = "Sanyukt"
    MAHILA = "Mahila"

    # Type of Gender
    MANDAL_TYPE_CHOICES = Choices(
        (BAL, 'Bal', _('Bal')),
        (BALIKA, 'Balika', _('Balika')),
        (YUVAK, 'Yuvak', _('Yuvak')),
        (YUVATI, 'Yuvati', _('Yuvati')),
        (SANYUKT, 'Sanyukt', _('Sanyukt')),
        (MAHILA, 'Mahila', _('Mahila')),
    )


class HaribhaktConstants(object):
    # Gender types
    MALE = "Male"
    FEMALE = "Female"
    TRANSGENDER = "Transgender"
    OTHER = "Other"

    # Type of Gender
    GENDER_CHOICES = Choices(
        (MALE, 'Male', _('Male')),
        (FEMALE, 'Female', _('Female')),
        (TRANSGENDER, 'Transgender', _('Transgender')),
        (OTHER, 'Other', _('Other')),
    )
