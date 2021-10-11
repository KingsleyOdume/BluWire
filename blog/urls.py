from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView, name='blog'),
    path('<slug:slug>/', views.BlogDetail, name='post_detail'),

]