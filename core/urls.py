from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/activar_clon/<int:clon_id>/', views.activar_clon, name='activar_clon'),
    path('home/activar_clon/', views.activar_clon, name='activar_clon'),
    path('ajax/lista_content/', views.lista_content, name='lista_content'),
    path('ajax/lista_content/<int:id_lista>/', views.lista_content,
         name='lista_content'),

    path('ajax/listas/', views.listas, name='listas'),
    path('ajax/clones/', views.clones, name='clones')
]
