from django.contrib import admin
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from import_export import resources

from .models import Customer
from .helpers import get_lat_lng


class CustomerResource(resources.ModelResource):
    """
    Class with a function before import to get the customers location by city
    """
    class Meta:
        model = Customer

    def before_import_row(self, row, **kwargs):
        row['gender'] = row['gender'].lower()
        if row['city']:
            geolocation = get_lat_lng(row['city'])
            try:
                row['latitude'] = geolocation[0]['latitude']
                row['longitude'] = geolocation[0]['longitude']
            except IndexError:
                pass


@admin.register(Customer)
class CustomerAdmin(ImportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'company',
        'city',
        'title',
    )
    search_fields = (
        'first_name',
        'last_name',
        'company',
        'city',
        'title',
    )

    formats = (base_formats.CSV,)
    resource_class = CustomerResource
