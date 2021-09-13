from django.urls import path
from product.views import *

urlpatterns = [
    path('all/', ProductsListCreateView.as_view(), name='publication-list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='publication-detail')
]
