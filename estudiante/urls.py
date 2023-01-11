from django.urls import path

from estudiante.views import saludar

urlpatterns = [
    path('saludar/', saludar),
]