from django.urls import path, include
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('go/', views.go, name='go'),
    path('save_visitor/<int:market_pk>/<int:user_pk>/', views.save_visitor, name='save_visitor'),
    path('qrcode_page/<int:market_pk>/<int:user_pk>/', views.qrcode_page, name='qrcode_page'),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    # 리뷰
    path('write_review/<int:market_pk>/', views.write_review, name='write_review'),
    path('get_review/<int:review_pk>/', views.get_review, name='get_review'),
    path('market_reviews/<int:market_pk>/', views.market_reviews, name='market_reviews'),
    path('ud_review/<int:review_pk>/', views.ud_review, name='ud_review'),
    # 상점
    path('write_store/<int:market_pk>/', views.write_store, name='write_store'),
    path('get_store/<int:store_pk>/', views.get_store, name='get_store'),
    path('market_stores/<int:market_pk>/', views.market_stores, name='market_stores'),
    path('ud_store/<int:store_pk>/', views.ud_store, name='ud_store'),
    # 물품
    path('write_item/<int:store_pk>/', views.write_item, name='write_item'),
    path('store_items/<int:store_pk>/', views.store_items, name='store_items'),
    path('ud_item/<int:item_pk>/', views.ud_item, name='ud_item'),

]