from django.contrib import admin
from django.urls import path, include
from tags.views import CreateTagView 

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create-tag'),    
]
