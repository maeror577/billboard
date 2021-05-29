from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserForm

from django.urls import reverse_lazy


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self, **kwargs):
        id = self.request.user.pk
        return User.objects.get(pk=id)


class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user_edit.html'
    form_class = UserForm
    success_url = reverse_lazy('user_detail')

    def get_object(self, **kwargs):
        id = self.request.user.pk
        return User.objects.get(pk=id)
