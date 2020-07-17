from django.urls import path, include
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('makevisitor/', views.makevisitor, name='makevisitor'),
    path('make_visitor_record/<int:market_pk>/',views.make_visitor_record,name='make_visitor_record'),
    path('qrcode_page/<int:market_pk>/<int:user_pk>/', views.qrcode_page, name='qrcode_page'),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
]