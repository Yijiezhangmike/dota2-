from django.urls import path
 
from . import views







app_name = 'login_app'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('password_reset_request/', views.password_reset_request, name='password_reset_request'),
    path('password_reset/', views.password_reset, name='password_reset_request'),

    path('redirect_register/', views.redirect_register, name='redirect_register'),
    path('redirect_register/register', views.register, name='register'),
    path('redirect_register/log', views.log, name='relog'),
    path('password_reset_request/password_reset', views.password_reset, name='password_reset'),
    path('log', views.log , name='log'),
    path('setcookie', views.setcookie ),
    path('showcookie', views.showcookie )
]