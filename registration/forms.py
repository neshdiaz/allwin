from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Jugador
from django.db import models


class RegistroReferidoForm(forms.Form):
    patrocinador = forms.CharField(max_length=50)


class UserCreationForm2(UserCreationForm):
    patrocinador = forms.CharField(max_length=50, required=False)
