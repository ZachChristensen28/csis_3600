from django.views.generic import TemplateView

# Create your views here.


class FirstClueView(TemplateView):
    template_name = 'secret/clue1.html'
