from django.views.generic import CreateView, UpdateView
# from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm


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
