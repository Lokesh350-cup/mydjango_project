#forms_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_name_views, name='form_name'),
]