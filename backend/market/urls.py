from django.urls import path, include
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('makevisitor/', views.makevisitor, name='makevisitor'),
    path('qrcode_page/', views.qrcode_page, name='qrcode_page'),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
]