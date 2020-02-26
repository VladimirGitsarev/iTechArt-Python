from django.conf.urls import url
from . import views

app_name = 'App'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.catalog, name='catalog')
]
