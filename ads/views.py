from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from .models import Ad, Offer
from .forms import AdForm


class AdList(LoginRequiredMixin, ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'
    ordering = ['-posted']


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

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        ad = self.get_object()
        if not (ad.author == user or user.is_superuser):
            raise PermissionDenied
        return handler


class AdDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'ads/ad_delete.html'
    queryset = Ad.objects.all()
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        ad = self.get_object()
        if not (ad.author == user or user.is_superuser):
            raise PermissionDenied
        return handler


class OfferListView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'ads/offers.html'
    context_object_name = 'offers'

    def get_queryset(self):
        context = Offer.objects.filter(ad__author=self.request.user)
        return context

    def accept(request, pk):
        offer = Offer.objects.get(pk=pk)
        offer.is_accepted = True
        offer.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class OfferDeleteView(LoginRequiredMixin, DeleteView):
    model = Offer
    success_url = reverse_lazy('offers')
