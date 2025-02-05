from django.urls import path 
from .views import UserRegister, EditProfileView , profile , Home


urlpatterns = [
    path('', Home.as_view(), name = "home"),
    path('register/', UserRegister.as_view(), name = 'register'),
    path('profile/<int:pk>', profile , name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name = 'profile-edit'),
]