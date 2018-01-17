from django.urls import path
from . import views


app_name = 'secret'

urlpatterns = [
    path('', views.FirstClueView.as_view(), name='clue1'),
]


handler404 = 'csis3600.views.handler404'
handler500 = 'csis3600.views.handler500'
