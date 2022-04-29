from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'main'

urlpatterns = [
    path('kettik', views.kettik, name='kettik'),
    path('main', views.main_page, name='main'),
    path('login', views.login, name='login'),
    path('search', views.search, name='search'),
    path('register', views.postsignUp, name='register')
]

urlpatterns += staticfiles_urlpatterns()