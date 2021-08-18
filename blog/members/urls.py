from django.urls import path
from .views import RegisterView, UserChangeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile/', UserChangeView.as_view(), name='edit_profile'),
]
