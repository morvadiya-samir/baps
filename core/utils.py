from django.conf import settings
from django.db import IntegrityError
import unicodecsv as csv
import json
from datetime import datetime, timedelta
from django.db.models import Q, Max
from django.http import HttpResponse

from .constants import *
from django.db import models


class FileData(object):
    @classmethod
    def create_haribhakt_data(cls, file):

        def _validate_phone_number(phone_number, field_name):
            # Validate phone number and set error if we found any error while validating phone number
            phone_error = ""
            try:
                phone_number = phone_number.strip()
                if len(phone_number) == 10:
                    phone_number = int(phone_number)
                    if any(u.contact_number == phone_number for u in user_data):
                        phone_error += field_name + ": Duplicate " + field_name + ". "
                else:
                    phone_error += field_name + ": Invalid " + field_name + ". "
                    return phone_number, phone_error

            except Exception as e:
                phone_error += field_name + ": Invalid " + field_name + ". "
            return phone_number, phone_error

        def _validate_boolean_fields(field_value, field_name):
            # Validate boolean value
            field_error = ""
            try:
                value_to_return = field_value.strip()
                if value_to_return.lower() == 'yes' or value_to_return.lower() == 'y':
                    value_to_return = True
                    return value_to_return, ''
                elif value_to_return.lower() == 'no' or value_to_return.lower() == 'n':
                    value_to_return = False
                    return value_to_return, ''
                else:
                    field_error += "Invalid value for" + field_name + ", "
                    return value_to_return, field_error
            except Exception as e:
                field_error += "Invalid value" + field_name + ", "
            return field_value, field_error

        def _validate_gender(field_value):
            # Validate boolean value
            field_error = ""
            try:
                value_to_return = field_value.strip()
                if value_to_return.lower() == HaribhaktConstants.MALE or value_to_return.lower() == 'm':
                    value_to_return = HaribhaktConstants.MALE
                    return value_to_return, ''
                elif value_to_return.lower() == HaribhaktConstants.FEMALE or value_to_return.lower() == 'f':
                    value_to_return = HaribhaktConstants.FEMALE
                    return value_to_return, ''
                elif value_to_return.lower() == HaribhaktConstants.OTHER or value_to_return.lower() == 'o':
                    value_to_return = HaribhaktConstants.OTHER
                    return value_to_return, ''
                else:
                    field_error += "Invalid value for Gender, "
                    return value_to_return, field_error
            except Exception as e:
                field_error += "Invalid value for Gender, "
            return field_value, field_error

        def _validate_date(date_value, field_name):
            """
            :param date_to_validate: date to be validated in dd/mm/yyyy %H:%M format
            :return: validated date and error text if any
            """
            date_error = ""
            date_to_return = ""
            try:
                date_to_return = date_value.strip()
                if date_to_return:
                    # parsing date to datetime field format
                    date_to_return = datetime.strptime(date_to_return, "%d/%m/%y")
                else:
                    date_error = field_name + " Can't be blank. "
            except Exception as e:
                date_error = field_name + " : Invalid format. Valid format is dd/mm/yy, "
            return date_to_return, date_error

        def _validate_duration(duration_value, field_name):
            duration_to_ret = 0
            duration_error = ""
            try:
                if duration_value:
                    duration_to_ret = int(duration_value)
            except ValueError as e:
                duration_error = "Invalid " + field_name + ". "
            return duration_to_ret, duration_error

        def _validate_string(field_value, field_name):
            """

            :param field_value:
            :param field_name:
            :return:
            """
            field_error = ""
            value_to_return = ""
            if field_value:
                value_to_return = field_value.strip()
            else:
                field_error += field_name + ": It can't be empty, "

            return value_to_return, field_error

        def _validate_integer(field_value, field_name):
            value_to_ret = 0
            field_error = ""
            try:
                if field_value:
                    value_to_ret = int(field_value)
            except ValueError as e:
                field_error = "Invalid " + field_name + ". "
            return value_to_ret, field_error

        file_data = file.get_file_data()
        user_data = []
        data_to_write_to_file = []
        is_error = False

        for data in file_data:
            error_text = ""

            name, name_error_text = _validate_string(data[FileConstants.NAME], FileConstants.NAME)
            if name_error_text:
                error_text += name_error_text

            is_gunbhavi, is_gunbhavi_error_text = _validate_boolean_fields(data[FileConstants.IS_GUNBHAVI],
                                                                           FileConstants.IS_GUNBHAVI)
            if is_gunbhavi_error_text:
                error_text += is_gunbhavi_error_text

            gender, gender_error_text = _validate_gender(data[FileConstants.GENDER])
            if gender_error_text:
                error_text += gender_error_text

            is_hof, is_hof_error_text = _validate_boolean_fields(data[FileConstants.IS_HOF], FileConstants.IS_HOF)
            if is_hof_error_text:
                error_text += is_hof_error_text

            relation_with_hof = data[FileConstants.RELATION_WITH_HOF] if data[FileConstants.RELATION_WITH_HOF] else ''

            hof = data[FileConstants.HOF]

            # validate PHONE NUMBER
            phone_number1, phone_number1_error_text = _validate_phone_number(data[FileConstants.CONTACT_NUM1],
                                                                             FileConstants.CONTACT_NUM1)
            if phone_number1_error_text:
                error_text += phone_number1_error_text

            phone_number2, phone_number2_error_text = _validate_phone_number(data[FileConstants.CONTACT_NUM2],
                                                                             FileConstants.CONTACT_NUM2)
            if phone_number2_error_text:
                error_text += phone_number2_error_text

            phone_number3, phone_number3_error_text = _validate_phone_number(data[FileConstants.CONTACT_NUM3],
                                                                             FileConstants.CONTACT_NUM3)
            if phone_number3_error_text:
                error_text += phone_number3_error_text

            dob, dob_error_text = _validate_date(data[FileConstants.DOB], FileConstants.DOB)
            if dob_error_text:
                error_text += dob_error_text

            satsang_duration, satsang_duration_text = _validate_duration(data[FileConstants.SATSANG_DURATION],
                                                                         FileConstants.SATSANG_DURATION)
            if satsang_duration_text:
                error_text += satsang_duration_text

            nitya_puja, nitya_puja_error_text = _validate_boolean_fields(data[FileConstants.NITYA_PUJA],
                                                                         FileConstants.NITYA_PUJA)
            if nitya_puja_error_text:
                error_text += nitya_puja_error_text

            tilak_chandlo, tilak_chandlo_error_text = _validate_boolean_fields(data[FileConstants.TILAK_CHAANDLO],
                                                                               FileConstants.TILAK_CHAANDLO)
            if tilak_chandlo_error_text:
                error_text += tilak_chandlo_error_text

            vyasan, vyasan_error_text = _validate_boolean_fields(data[FileConstants.VYASAN], FileConstants.VYASAN)
            if vyasan_error_text:
                error_text += is_hof_error_text

            vyasan_type = data[FileConstants.VYASAN] if data[FileConstants.VYASAN] else ''

            onion_garlic, onion_garlic_error_text = _validate_boolean_fields(data[FileConstants.ONION_GARLIC],
                                                                             FileConstants.ONION_GARLIC)
            if onion_garlic_error_text:
                error_text += onion_garlic_error_text

            weekly_sabha, vyasan_error_text = _validate_boolean_fields(data[FileConstants.VYASAN], FileConstants.VYASAN)
            if vyasan_error_text:
                error_text += is_hof_error_text

            poonam_sabha, poonam_sabha_error_text = _validate_boolean_fields(data[FileConstants.POONAM_SABHA],
                                                                             FileConstants.POONAM_SABHA)
            if poonam_sabha_error_text:
                error_text += poonam_sabha_error_text

            ghar_sabha, ghar_sabha_error_text = _validate_boolean_fields(data[FileConstants.POONAM_SABHA],
                                                                         FileConstants.POONAM_SABHA)
            if ghar_sabha_error_text:
                error_text += ghar_sabha_error_text

            vachnamrut_swami_ni_vaato, vachnamrut_swami_ni_vaato_error_text = _validate_boolean_fields(
                data[FileConstants.VACHNAMURT_SWAMI_VAATO], FileConstants.VACHNAMURT_SWAMI_VAATO)
            if vachnamrut_swami_ni_vaato_error_text:
                error_text += vachnamrut_swami_ni_vaato_error_text

            ssp, ssp_error_text = _validate_boolean_fields(data[FileConstants.SSP], FileConstants.SSP)
            if ssp_error_text:
                error_text += ssp_error_text

            monthly_donation, monthly_donation_error_text = _validate_integer(data[FileConstants.MONTHLY_DONATION],
                                                                              FileConstants.MONTHLY_DONATION)
            if monthly_donation_error_text:
                error_text += monthly_donation_error_text

            if error_text:
                is_error = True
                error_text = error_text[:-2]

            mandal_instance = models.Mandal.objects.get(id=1)
            # temp
            hof_instance = models.Haribhakt.objects.get(id=3)
            if not error_text:
                user_data.append(
                    models.Haribhakt(file=file, mandal=mandal_instance, name=name, is_gunbhavi=is_gunbhavi,
                                     gender=gender, is_head_of_family=is_hof, relation_with_hof=relation_with_hof,
                                     head_of_family=hof_instance, contact_number_1=phone_number1, contact_number_2=phone_number2,
                                     contact_number_3=phone_number3, birth_date=dob,
                                     number_of_years_of_satsang=satsang_duration, nitya_pooja=nitya_puja,
                                     tilak_chaandlo=tilak_chandlo, vyasan=vyasan, vyasan_type=vyasan_type,
                                     onion_garlic=onion_garlic, weekly_sabha=weekly_sabha, poonam_sabha=poonam_sabha,
                                     ghar_sabha=ghar_sabha, vachnamrut_swami_ni_vaato_vanchan=vachnamrut_swami_ni_vaato,
                                     satsang_sikshan_pariksha=ssp, monthtly_donation=monthly_donation)
                )

            data_of_headers = []
            for header in FileConstants.HARIBHAKTO_FILE_HEADERS:
                data_of_headers.append(data[header])
            data_of_headers.append(error_text)

            data_to_write_to_file.append(data_of_headers)

        if not is_error:
            models.Haribhakt.objects.bulk_create(user_data)

        file_name = 'haribhakto' + str(datetime.now()) + '.csv'
        return csv_http_response(data_to_write_to_file, file.get_csv_file_headers(),
                                 file_name=file_name)


def get_valid_filters(filters):
    """

    :param filters:
    :return: return the filters removing the keys with empty values
    """
    try:
        return {k: v for k, v in filters.items() if str(v)}
    except Exception as e:
        return {}


def csv_http_response(data, file_headers, file_name="dg.csv", display_error_column=True):
    """

    :param data: Data to write in CSV file
    :param file_headers: Headers to write in the csv file
    :param file_name: File name when the CSV file is exported as a HTTP response
    :return: CSV response file for given headers and data
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + file_name + '"'
    writer = csv.writer(response)
    if display_error_column:
        writer.writerow(file_headers + ["Error"])
    else:
        if file_headers:
            writer.writerow(file_headers)
    writer.writerows(data)
    return response
