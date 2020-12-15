from django.urls import path
from django.conf.urls import url
from .views import ItemView, ItemCreateView, ItemUpdateView

urlpatterns = [
    path('api/', ItemView.as_view()),
    path('api/create', ItemCreateView.as_view()),
    path('api/update/<int:pk>', ItemUpdateView.as_view())
]