"""decade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from member.serializers import UserViewSet
from cargo.viewsets import CargoViewSet
from client.viewsets import ClientViewSet, CompanyViewSet
from depot.viewsets import DepotViewSet
from invoice.viewsets import InvoiceViewSet
from order.viewsets import OrderViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cargo', CargoViewSet)
router.register(r'client', ClientViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'depot', DepotViewSet)
router.register(r'invoice', InvoiceViewSet)
router.register(r'order', OrderViewSet)
            
urlpatterns = [
    path('Haha_U_Bro_hmmm/', admin.site.urls),
    re_path(r'^api/v1/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]
