from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms


class NewRegisterForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Nombres'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Apellidos'}))
    alias = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Alias'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Correo Electónico'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password',
                                                                 'type': 'password'}))


# Create your views here.

def index(request):
    return render(request, "console/index.html")


def register(request):
    return render(request, "console/register.html", {
        "form": NewRegisterForm()
    })
