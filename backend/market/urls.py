from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('write_review/<int:market_pk>/', views.write_review, name='write_review'),
    path('get_review/<int:review_pk>/', views.get_review, name='get_review'),
    path('market_review/<int:market_pk>/', views.market_review, name='market_review'),
    path('ud_review/<int:review_pk>/', views.ud_review, name='ud_review'),
]