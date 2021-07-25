from django.urls import include, path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index')
]