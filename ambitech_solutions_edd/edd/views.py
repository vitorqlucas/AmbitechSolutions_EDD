from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_edd(request):
    erro = False

    # Verifica se o usuário já está autenticado
    if request.user.is_authenticated:
        return redirect('edd')

    if request.method == "POST":
        username = request.POST.get("username")  # Captura o username do formulário
        password = request.POST.get("password")  # Captura a senha do formulário

        if username and password:
            # Autentica o usuário usando username e senha
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)  # Faz o login
                return redirect('edd')
            else:
                erro = True  # Credenciais inválidas
        else:
            erro = True  # Campos vazios

    return render(request, 'user/login_edd.html', {"erro": erro})


@login_required
def edd(request):
    return render(request, 'edd.html')


@login_required
def atualizacoes(request):
    return render(request, 'atualizacoes.html')


def logout_view(request):
    logout(request)
    return redirect('login_edd')

