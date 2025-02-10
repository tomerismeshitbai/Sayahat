from django.shortcuts import render , redirect , get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from django.urls import reverse_lazy
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import TemplateView 
from rest_framework import viewsets
from .serializers import ProfileSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework.views import APIView

#drf
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": response.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })
        
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist() 
            return Response({"message": "Successfully logged out"}, status=200)
        except Exception as e:
            return Response({"error": "Invalid refresh token"}, status=400)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



#django
class Home(TemplateView):
    template_name = 'home.html'

class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)  
        return super().form_valid(form)

class EditProfileView(generic.UpdateView):
    form_class = ProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user.profile
    
def profile(request, pk):
    user = get_object_or_404(User, id = pk)
    profile = get_object_or_404(Profile, user=user)
    users = User.objects.exclude(id=request.user.id)
    return render(request, "profile.html")