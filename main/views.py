from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect


def kettik(request):
    return render(request, 'main/homepage.html')


def main_page(request):
    return render(request,'main/index.html')