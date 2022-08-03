from . import views
from django.urls import path

urlpatterns = [
    path('',views.load_add_page,name='load_add_page'),
    path('add_num',views.add_num,name='add_num'),
    path('load_home_page',views.load_home_page,name='load_home_page'),

]
