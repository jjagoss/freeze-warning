from django.urls import path

from . import views

app_name = 'berkeley'

urlpatterns = [
    path('/', views.index, name='index'),
]
