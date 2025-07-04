from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contact:user_update')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')







# @login_required

# from django.contrib import auth, messages
# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import redirect, render

# from contact.forms import RegisterForm


# def register(request):
#     form = RegisterForm()

#     if request.method == 'POST':
#         form = RegisterForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Usuário registrado')
#             return redirect('contact:login')

#     return render(
#         request,
#         'contact/register.html',
#         {
#             'form': form
#         }
#     )


# def login_view(request):
#     form = AuthenticationForm(request)

#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)

#         if form.is_valid():
#             user = form.get_user()
#             auth.login(request, user)
#             messages.success(request, 'Logado com sucesso!')
#             return redirect('contact:index')
#         messages.error(request, 'Login inválido')

#     return render(
#         request,
#         'contact/login.html',
#         {
#             'form': form
#         }
#     )


# def logout_view(request):
#     auth.logout(request)
#     return redirect('contact:login')








# from django.contrib import messages
# from django.shortcuts import render, redirect

# from contact.forms import RegisterForm


# def register(request):
#     form = RegisterForm()

#     # messages.info(request, 'Mensagem de teste')
#     # messages.success(request, 'Registro criado com sucesso')
#     # messages.error(request, 'Erro ao criar o registro')
#     # messages.warning(request, 'Aviso: algo não está certo')


#     if request.method == 'POST':
#         form = RegisterForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registro criado com sucesso')
#             return redirect('contact:index')

#     return render(
#         request,
#         'contact/register.html',
#         {
#             'form': form
#         }
#     )
