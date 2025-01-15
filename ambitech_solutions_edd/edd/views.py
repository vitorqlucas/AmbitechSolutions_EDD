from django.shortcuts import render

# Toda função em uma view precisa retornar alguma coisa
def login_edd(request):
    return render(request, 'login_edd.html')

def edd(request):
    return  render(request, 'edd.html')
# Create your views here.
