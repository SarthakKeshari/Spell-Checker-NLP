from django.contrib import admin
from django.urls import path, include
from SpellCheckApp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('word_check.html', views.word_check, name="word_check"),
    path('sentence_check.html', views.sentence_check, name="sentence_check"),
    path('document_check.html', views.document_check, name="document_check"),
    path('website_info.html', views.website_info, name="website_info"),
    path('about.html', views.about, name="about"),
    path('reference.html', views.reference, name="reference"),
]