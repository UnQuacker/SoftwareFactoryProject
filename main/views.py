from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect


def kettik(request):
    return render(request, 'main/homepage.html')


def main_page(request):
    return render(request, 'main/index.html')


def register(request):
    return render(request, 'main/registerligin.html')


def search(request):
    return render(request, 'main/search.html')
