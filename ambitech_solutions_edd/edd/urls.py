from tkinter.font import names

from django.urls import path
from.views import *


urlpatterns = [
    path('loginedd', login_edd, name='login_edd'), #link, função, nome interno da sua pagina
    path('edd', edd, name='edd'),
    path('atualizacoes', atualizacoes, name='atualizacoes')
]