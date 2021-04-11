from django.urls import path
from .views import ListProductView, ListPromotionView

urlpatterns = [
    path('listproduct/',ListProductView.as_view(),name='listproduct'),
    path('listpromotion/',ListPromotionView.as_view(),name='listpromotion')
]



