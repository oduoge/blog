from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/query/', views.query, name='query'),
    url(r'^$', views.login, name='login'),
]