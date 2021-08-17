from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm


class RegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
