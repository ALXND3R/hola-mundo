# pagina_web/urls.py
from django.urls import path
from .views import VistaPaginaDeInicio

urlpatterns = [path("", VistaPaginaDeInicio, name="PaginaInicio")]
