from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from registration.forms import UserCreationForm2
from django import forms
from django.db import transaction
from core.models import Jugador


def registro_referido(request, patrocinador):

    if User.objects.filter(username=patrocinador).exists():
        referido_valid = True
    else:
        referido_valid = False
    return render(request, 'registration/registro_referido.html',
                           {'patrocinador': patrocinador,
                            'referido_valid': referido_valid
                            }
                  )


class login(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/login.html'

    def get_form(self, form_class=None):
        form = super(login, self).get_form()
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2',
                   'placeholder': 'Nombre de Usuario'})
        form.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2',
                   'placeholder': 'Contraseña'})
        return form


class logged_out(LogoutView):
    next_page = reverse_lazy('registration:login')
    template_name = 'registration/logged_out.html'


class RegistroUsuario(CreateView):
    form_class = UserCreationForm2
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

    def get_form(self, form_class=None):
        form = super(RegistroUsuario, self).get_form()
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2',
                   'placeholder': 'Nombre de Usuario'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2',
                   'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2',
                   'placeholder': 'Confirme su contraseña'})

        form.fields['patrocinador'].widget = forms.HiddenInput()
        return form

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save()
        self.object.refresh_from_db()
        user = User.objects.get(username=form['username'].data)
        if str(form['patrocinador'].data) == '':
            pat = Jugador.objects.filter(usuario__username='System')
            if pat.exists():
                j = Jugador(usuario=user, patrocinador=pat[0])
            else:
                j = Jugador(usuario=user)
        else:
            user_patrocinador = User.objects.get(
                username=form['patrocinador'].data)
            patrocinador = Jugador.objects.get(
                usuario=user_patrocinador)
            j = Jugador(usuario=user, patrocinador=patrocinador)
        j.save()
        return super().form_valid(form)
