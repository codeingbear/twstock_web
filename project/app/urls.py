from django.urls import path
from . import views
urlpatterns=[
    path('',views.main),
    path('<int:stock_num>/',views.num),
    path('<str:stock_name>/',views.name),
]