from django.views.generic import CreateView, UpdateView
# from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm


class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('change_success')


def ChangeSuccess(request):

    return render(request, 'registration/success.html', {})


class RegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserChangeView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
