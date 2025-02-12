from django.urls import path, include
from .views import UserRegister, EditProfileView , profile , Home , RegisterView, ProfileViewSet, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet) 

urlpatterns = [
    path('', Home.as_view(), name = "home"),
    path('register/', UserRegister.as_view(), name = 'register'),
    path('profile/<int:pk>', profile , name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name = 'profile-edit'),
    
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    path('api/register/', RegisterView.as_view(), name='api-register'),
]