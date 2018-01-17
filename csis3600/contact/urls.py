from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.CreateContact.as_view(), name='contactForm'),
    path('thank-you-now-get-out-of-here/',
         views.Success.as_view(), name='success'),
]

handler404 = 'csis3600.views.handler404'
handler500 = 'csis3600.views.handler500'
