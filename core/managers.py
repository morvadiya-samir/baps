from __future__ import unicode_literals
from django.db.models import Manager
from django.db.models import Q

from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
# from django_bulk_update.manager import BulkUpdateManager
from .utils import FileData
from .utils import get_valid_filters


class BaseManager(Manager):
    def active(self):
        """Return only active(un-deleted) items in the current queryset"""
        return self.exclude(status=self.model.DELETED)

    def deleted(self):
        """Return only deleted items in the current queryset"""
        return self.filter(status=self.model.DELETED)

    def activate_all(self):
        """ Activate all """
        return self.all().update(status=self.model.ACTIVE)

    def delete_all(self):
        """ Activate all """
        return self.all().update(status=self.model.DELETED)


class HaribhaktManager(BaseManager):
    def create_from_file(self, file_obj):
        """
            This is a model method to convert a file object into corresponding call data objects
            Responsibility:
                1. Get json from file
                2. Loop around the json data and create CallData instances
                3. Save CallData intances in bulk
        """
        response = FileData.create_haribhakt_data(file_obj)
        return response


class FileManager(BaseManager):
    pass
