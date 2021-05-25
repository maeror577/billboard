from django.urls import path
from .views import (AdList, AdDetailView, AdCreateView,
                    AdEditView, AdDeleteView)


urlpatterns = [
    path('', AdList.as_view()),
    path('<int:pk>', AdDetailView.as_view(), name='ad_detail'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('update/<int:pk>/', AdEditView.as_view(), name='ad_edit'),
    path('delete/<int:pk>/', AdDeleteView.as_view(), name='ad_delete'),
]
