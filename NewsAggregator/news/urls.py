from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('upload', views.upload,  name='upload-file'),
    path('uploadfile', views.uploadfile, name='upload-file'),
    #path('createcountry', views.uploadfile, name='upload-file'),

    path('about/', views.about, name='news-about'),
    path('gonews', views.gonews, name='news-home'),
    ]
