from django_filters import FilterSet
from .models import Offer


class OfferFilter(FilterSet):
    class Meta:
        model = Offer
        fields = ['ad']
