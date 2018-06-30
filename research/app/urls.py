from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add', views.add, name='add'),
    url(r'edit/(?P<p_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'delete/(?P<p_id>[0-9]+)/', views.delete, name='delete'),
]