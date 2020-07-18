from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    # 리뷰
    path('write_review/<int:market_pk>/', views.write_review, name='write_review'),
    path('get_review/<int:review_pk>/', views.get_review, name='get_review'),
    path('market_review/<int:market_pk>/', views.market_review, name='market_review'),
    path('ud_review/<int:review_pk>/', views.ud_review, name='ud_review'),
    # 상점
    path('write_store/<int:market_pk>/', views.write_store, name='write_store'),
    path('get_store/<int:store_pk>/', views.get_store, name='get_store'),
    path('market_store/<int:market_pk>/', views.market_store, name='market_store'),
    path('ud_store/<int:store_pk>/', views.ud_store, name='ud_store'),
]