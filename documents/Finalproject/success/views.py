from django.shortcuts import render
from django.http import HttpResponse


def index(request, *args, **kwargs):
    return render(request, 'index.html', {})


def about(request, *args, **kwargs):
    return render(request, 'about.html', {})


def services(request, *args, **kwargs):
    return render(request, 'services.html', {})


def safety(request, *args, **kwargs):
    return render(request, 'safety.html', {})


def contact(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def pay_bill(request, *args, **kwargs):
    return render(request, 'pay_bill.html', {})


def blog(request, *args, **kwargs):
    return render(request, 'blog.html', {})
