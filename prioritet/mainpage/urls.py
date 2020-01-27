from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^cabinet/', views.cabinet, name='cabinet'),
    url(r'^about/', views.about, name='about'),
    url(r'^service/', views.service, name='service'),
    url(r'^uslugi/', views.uslugi, name='uslugi')
]