from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from .forms import UserRegisterForm, UserProfileForm


class UserRegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        contex = {
            'form': UserRegisterForm(),
        }

        return render(request, self.template_name, contex)

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))
