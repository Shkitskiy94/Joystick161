from django.urls import reverse_lazy
from django.views.generic import CreateView

from .form import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('store:home')
    template_name = 'users/signup.html'
