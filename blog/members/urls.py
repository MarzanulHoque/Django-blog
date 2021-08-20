from django.urls import path
from .views import RegisterView, UserChangeView, PasswordsChangeView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile/', UserChangeView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('change_success/', views.ChangeSuccess, name='change_success'),


]
