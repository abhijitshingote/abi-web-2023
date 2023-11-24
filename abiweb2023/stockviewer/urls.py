from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_stocks, name="list_stocks"),
    path("<symbol>", views.stock_detail, name="stock_detail"),
]