from django.conf.urls import url
from .views import NameList
from . import views

urlpatterns = [
    # expense/
    url(r'^$', NameList.as_view(), name = 'list'),
    url(r'^success$', views.ImportCsv, name='success'),
    url(r'^table$', views.Table, name='table'),
]