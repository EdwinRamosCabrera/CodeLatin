from django.urls import path
from . import views

app_name = 'auths'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('activate_account/<uidb64>/<token>/', views.verify_account, name='activate_account'),

]
