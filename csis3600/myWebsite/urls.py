from django.urls import path
from . import views

app_name = 'myWebsite'

urlpatterns = [
    path('week-1/', views.Week1.as_view(), name='week1'),
    path('week-2/', views.Week2.as_view(), name='week2'),
    path('week-3/', views.Week3.as_view(), name='week3'),
    path('week-4/', views.Week4.as_view(), name='week4'),
    path('week-5/', views.Week5.as_view(), name='week5'),
    path('week-6/', views.Week6.as_view(), name='week6'),
    path('week-7/', views.Week7.as_view(), name='week7'),
    path('week-8/', views.Week8.as_view(), name='week8'),
]
