from django.urls import path
 
from . import views
app_name = 'dota2_deco'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('search/',views.search, name='search'),
    path('publish/',views.publish, name='publish'),
    path('publish/item_upload/',views.item_upload, name='item_upload'),
]
