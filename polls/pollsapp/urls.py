from django.urls import include, path

from . import views

app_name = 'polls'
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', views.index, name='index')
]