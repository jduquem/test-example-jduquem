from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.views import View
from Aplicaciones.Transporte.forms import UserRegisterForm, UserLoginForm

class RegisterUser(View):
    template_name = 'signup.html'    
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm(request.GET)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data['username']
            #messages.success(request, 'Usuario {} creado con exito.'.format(username))
            return redirect('home')
        else:
            #messages.success(request, 'Error de registro')
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


class LoginUser(View):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        form = UserLoginForm(request.GET)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, 'Bienvenido {}'.format(username))
                return redirect('/')
            else:
                #messages.success(request, 'Ocurrió un error')
                return redirect('/')
        else:
            #messages.success(request, 'Error de ingreso')
            return redirect('/')
        return render(request, self.template_name, {'form': form})
