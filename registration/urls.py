from django.urls import path
from . import views
from .views import RegistroUsuario, login, logged_out, registro_referido

app_name = 'registration'

urlpatterns = [
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    path('registro/<patrocinador>/', views.registro_referido,
         name='registro_referido'),
    path('login/', login.as_view(), name='login'),
    path('logged_out/', logged_out.as_view(), name='logged_out'),
]
