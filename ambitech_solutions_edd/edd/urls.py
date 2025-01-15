from django.urls import path
from.views import *

urlpatterns = [
    path('login_edd', login_edd, name='login_edd'), #link, função, nome interno da sua pagina
    path('edd', edd, name='edd')
]