from django.conf.urls import url
from .views import HomePage, MonthlyExpenseList
from . import views

urlpatterns = [
    # expense/
    url(r'^$', HomePage.as_view(), name = 'list'),
    url(r'^success$', views.ImportCsv, name='success'),
    url(r'^table$', MonthlyExpenseList.as_view(), name='table'),
]