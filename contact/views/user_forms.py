from django.contrib import messages
from django.shortcuts import render, redirect

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    # messages.info(request, 'Mensagem de teste')
    # messages.success(request, 'Registro criado com sucesso')
    # messages.error(request, 'Erro ao criar o registro')
    # messages.warning(request, 'Aviso: algo não está certo')


    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
