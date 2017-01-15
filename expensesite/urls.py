from django.conf.urls import url
from . import views

app_name = 'expense'
urlpatterns = [
    # expense/
    url(r'^$', views.mainpage, name = 'mainpage'),
]