"""
oowlish_challenge URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from customers.views import (
    CustomersViewSet,
    CustomerViewSet,
    CustomersView,
)


router = routers.DefaultRouter()
router.register(r'customers', CustomersViewSet)
router.register(r'customers-by-id', CustomerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', CustomersView.as_view(), name='customers'),
]
