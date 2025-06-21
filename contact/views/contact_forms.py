from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )








# from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse

# from contact.forms import ContactForm
# from contact.models import Contact


# def create(request):
#     form_action = reverse('contact:create')

#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         context = {
#             'form': form,
#             'form_action': form_action,
#         }

#         if form.is_valid():
#             contact = form.save()
#             return redirect('contact:update', contact_id=contact.pk)

#         return render(
#             request,
#             'contact/create.html',
#             context
#         )

#     context = {
#         'form': ContactForm(),
#         'form_action': form_action,
#     }

#     return render(
#         request,
#         'contact/create.html',
#         context
#     )


# def update(request, contact_id):
#     contact = get_object_or_404(
#         Contact, pk=contact_id, show=True
#     )
#     form_action = reverse('contact:update', args=(contact_id,))

#     if request.method == 'POST':
#         form = ContactForm(request.POST, instance=contact)

#         context = {
#             'form': form,
#             'form_action': form_action,
#         }

#         if form.is_valid():
#             contact = form.save()
#             return redirect('contact:update', contact_id=contact.pk)

#         return render(
#             request,
#             'contact/create.html',
#             context
#         )

#     context = {
#         'form': ContactForm(instance=contact),
#         'form_action': form_action,
#     }

#     return render(
#         request,
#         'contact/create.html',
#         context
#     )


# def delete(request, contact_id):
#     contact = get_object_or_404(
#         Contact, pk=contact_id, show=True
#     )
#     confirmation = request.POST.get('confirmation', 'no')

#     if confirmation == 'yes':
#         contact.delete()
#         return redirect('contact:index')

#     return render(
#         request,
#         'contact/contact.html',
#         {
#             'contact': contact,
#             'confirmation': confirmation,
#         }
#     )








# from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse

# from contact.forms import ContactForm
# from contact.models import Contact


# def create(request):
#     form_action = reverse('contact:create')

#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         context = {
#             'form': form,
#             'form_action': form_action,
#         }

#         if form.is_valid():
#             contact = form.save()
#             return redirect('contact:update', contact_id=contact.pk)

#         return render(
#             request,
#             'contact/create.html',
#             context
#         )

#     context = {
#         'form': ContactForm(),
#         'form_action': form_action,
#     }

#     return render(
#         request,
#         'contact/create.html',
#         context
#     )


# def update(request, contact_id):
#     contact = get_object_or_404(
#         Contact, pk=contact_id, show=True
#     )
#     form_action = reverse('contact:update', args=(contact_id,))

#     if request.method == 'POST':
#         form = ContactForm(request.POST, instance=contact)

#         context = {
#             'form': form,
#             'form_action': form_action,
#         }

#         if form.is_valid():
#             contact = form.save()
#             return redirect('contact:update', contact_id=contact.pk)

#         return render(
#             request,
#             'contact/create.html',
#             context
#         )

#     context = {
#         'form': ContactForm(instance=contact),
#         'form_action': form_action,
#     }

#     return render(
#         request,
#         'contact/create.html',
#         context
#     )








# from django.shortcuts import render

# from contact.forms import ContactForm


# def create(request):
#     if request.method == 'POST':
#         context = {
#             'form': ContactForm(request.POST)
#         }

#         return render(
#             request,
#             'contact/create.html',
#             context
#         )

#     context = {
#         'form': ContactForm()
#     }

#     return render(
#         request,
#         'contact/create.html',
#         context
#     )








# from typing import Any, Dict

# from django import forms
# from django.core.exceptions import ValidationError
# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.shortcuts import get_object_or_404, redirect, render

# from contact.models import Contact


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = (
#             'first_name', 'last_name', 'phone',
#         )

#     def clean(self):
#         cleaned_data = self.cleaned_data

#         self.add_error(
#             'first_name',
#             ValidationError(
#                 'Mensagem de erro',
#                 code='invalid'
#             )
#         )
#         self.add_error(
#             'first_name',
#             ValidationError(
#                 'Mensagem de erro 2',
#                 code='invalid'
#             )
#         )

#         return super().clean()


# def create(request):
#     if request.method == 'POST':
#         context = {
#             'form': ContactForm(request.POST)
#         }

#         return render(
#             request,
#             'contact/create.html',
#             context
#         )

#     context = {
#         'form': ContactForm()
#     }

#     return render(
#         request,
#         'contact/create.html',
#         context
#     )








# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.shortcuts import get_object_or_404, redirect, render

# from contact.models import Contact


# def create(request):
#     if request.method == 'POST':
#         print()
#         print(request.method)
#         print(request.POST.get('first_name'))
#         print(request.POST.get('last_name'))
#         print()

#     context = {

#     }

#     print()
#     print(request.method)
#     print()

#     return render(
#         request,
#         'contact/create.html',
#         context
#     )








# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.shortcuts import get_object_or_404, redirect, render

# from contact.models import Contact


# def create(request):
#     context = {

#     }

#     return render(
#         request,
#         'contact/create.html',
#         context
#     )
