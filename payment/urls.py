from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^page1/$', views.page1, name='process'),
    url(r'^page2/$', views.page2, name='page2'),
]