from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('write_review',views.write_review,name='write_review'),
]