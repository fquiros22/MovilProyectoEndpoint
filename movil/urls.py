from django.urls import path
from . import views

urlpatterns = [
    path("api/movil/", views.endPointMovil, name='endpoint'),
]