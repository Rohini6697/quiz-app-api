from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('api/all',views.quiz_list),
    path('api/add',views.add_quiz)
]