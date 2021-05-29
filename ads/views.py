from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin)

from .models import Ad, Response
from .forms import AdForm


class AdList(LoginRequiredMixin, ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'
    ordering = ['-posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_ads'] = Ad.objects.all()
        return context


class AdDetailView(LoginRequiredMixin, DetailView):
    template_name = 'ads/ad_detail.html'
    queryset = Ad.objects.all()


class AdCreateView(LoginRequiredMixin, CreateView):
    template_name = 'ads/ad_create.html'
    form_class = AdForm
    success_url = '/'


class AdEditView(LoginRequiredMixin, UpdateView):
    template_name = 'ads/ad_create.html'
    form_class = AdForm
    success_url = '/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)


class AdDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'ads/ad_delete.html'
    queryset = Ad.objects.all()
    success_url = '/'


class ResponsesListView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'ads/responses.html'
    context_object_name = 'responses'

    def get_queryset(self):
        context = Response.objects.filter(ad__author=self.request.user)
        return context
