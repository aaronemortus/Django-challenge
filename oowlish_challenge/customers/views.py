import markdown
from django.conf import settings
from django.urls import reverse
from urllib.parse import urljoin
from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import TemplateView

from .models import Customer
from .serializers import CustomerSerializer


class CustomersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ## API LISTING ALL CUSTOMERS

    Whole request are made over: ```http://localhost/api/customers-by-id/```
    """
    queryset = Customer.objects.all()
    http_method_names = ['get',]
    serializer_class = CustomerSerializer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ## API WITH A FILTER FOR GETTING A SINGLE CUSTOMER

    This API only accepts request in GET method

    ### Valid Filter fields from backend:

    * `id` Identifier code for customer

    ### Pagination options:

    * This API have a pagination with 100 registers. You can find
    it on the right side

    ### Example:

    Whole request are made over: ```http://localhost/api/customers-by-id/```

    _Request by id:_

    ```
    http GET {{host}}?id=20
    ```

    _if you want to add more filters, please contact the developer
    of this project._
    """
    queryset = Customer.objects.all()
    http_method_names = ['get',]
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id',]


class CustomersView(TemplateView):
    """
    View to render data from API, it could be posible rendering data directly
    from the model but for testing purposes the view is consuming from the API
    URL sending the URL as a context with json format and rendered from
    front-end
    """
    template_name = 'customers.html'

    def get_context_data(self, **kwargs):
        api_url = urljoin(settings.SITE_URL, '/api/customers/')
        context = super(CustomersView, self).get_context_data(**kwargs)
        data = {
            'api_url': api_url,
            'google_api': settings.GOOGLE_API_KEY,
        }
        context.update(data)
        return context
