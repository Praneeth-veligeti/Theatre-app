from django.urls import path
from . import views
urlpatterns=[
    path('', views.main, name='main'),
    path('occupy/<str:pname>',views.occupy, name='occupy'),
    path('vacate/<int:sn>', views.vacate, name='vacate'),
    path('get_info/<str:pname>', views.get_info, name='get_info'),
]