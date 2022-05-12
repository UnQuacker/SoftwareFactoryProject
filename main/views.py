import random
import traceback

import django_filters
from django.forms import CheckboxSelectMultiple
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, JsonResponse
import pyrebase
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Place
from .serializers import PlaceSerializer # PropertyFilter
from rest_framework.generics import ListAPIView
from rest_framework import filters


firebaseConfig = {
    'apiKey': "AIzaSyA7AKnjaTU0PdvPVC0IrlxyDTktHwSG4AA",
    'authDomain': "software-factory-ce597.firebaseapp.com",
    'projectId': "software-factory-ce597",
    'storageBucket': "software-factory-ce597.appspot.com",
    'messagingSenderId': "160550003152",
    'appId': "1:160550003152:web:1c02e7bfdf36959fa519d5",
    'measurementId': "G-EVZTV7SBHL",
    'databaseURL': ""

}
firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()


def kettik(request):
    return render(request, 'main/homepage.html')


def main_page(request):
    return render(request, 'main/index.html')


def register(request):
    return render(request, 'main/registerligin.html')


def search(request):
    return render(request, 'main/search.html')


def login(request):
    return render(request, 'main/login.html')


def postLogin(request):
    if request.method == 'POST':
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')
        try:
            user = authe.sign_in_with_email_and_password(email, password)
            return
        except:
            message = "Invalid credentials!"
            return render(request, 'main/registerligin.html', {'loginMessage': message})
    return render(request, 'main/index.html')


def postsignUp(request):
    if request.method == 'POST':
        emailReg = request.POST.get('register_email', False)
        passsReg = request.POST.get('register_password1')
        nameReg = request.POST.get('register_name')

        emailLog = request.POST.get('login_email', False)
        passwordLog = request.POST.get('login_password')
        if emailReg:
            try:
                # creating a user with the given email and password
                user = authe.create_user_with_email_and_password(emailReg, passsReg)
                uid = user['localId']
                idtoken = request.session['uid']
                # print(uid)
                return render(request, "main/homepage.html")
            except Exception as e:
                message = "invalid credentials!"
                return render(request, 'main/registerligin.html', {'message': message})
                pass
        elif emailLog:
            try:
                user = authe.sign_in_with_email_and_password(emailLog, passwordLog)
                return render(request, "main/homepage.html")
            except Exception as e:
                message = "invalid credentials!"
                return render(request, 'main/registerligin.html', {'loginMessage': message})
    else:
        return render(request, 'main/registerligin.html')
    # return render(request, "main/homepage.html")


class PlaceListAPIView(ListAPIView):

    filter_backends = (filters.SearchFilter,)
    search_fields = ['tags__name', ]
    serializer_class = PlaceSerializer
    model = Place
    queryset = Place.objects.all()

    # queryset = Place.objects.all()
    # serializer_class = PlaceSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['tags']


@csrf_exempt
def random_place(request):
    if request.method == 'GET':
        articles = list(Place.objects.all())
        random_article = random.choice(articles)
        serializer = PlaceSerializer(random_article)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlaceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)


def place(request):
    articles = list(Place.objects.all())
    random_article = random.choice(articles)
    print("Place Name:", random_article.name)
    print("Place Image:", random_article.place_image)
    print("Place URL", random_article.place_url)
    return render(request, 'main/rand.html', {'place': random_article})

