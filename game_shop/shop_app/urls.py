from django.urls import path
from . import views

app_name = "shop_app"

urlpatterns = [
    path("", views.main, name="main"),
    path("<int:page>", views.main, name="main_paginate"), 
    path("search/", views.search_results, name="search_result"),
    path("<str:game_title>/", views.game_detail, name="game_detail"), 
]