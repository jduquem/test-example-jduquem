from django.shortcuts import render
from django.views import View


#Clave API : AIzaSyB0CdWrNiCOjzJ4Ogq6c1VzK1KqXkez3ko
class Home(View):
    template_name = 'blank.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)