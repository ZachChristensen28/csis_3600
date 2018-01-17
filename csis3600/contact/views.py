from django.views.generic import CreateView, TemplateView
from .models import Contact


class CreateContact(CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'email', 'comments']


class Success(TemplateView):
    template_name = 'contact/success.html'
