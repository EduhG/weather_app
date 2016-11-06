from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^json_temps', views.get_json_temps, name='json_temps'),
]
