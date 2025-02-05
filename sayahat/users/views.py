from django.shortcuts import render , redirect , get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from django.urls import reverse_lazy
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import TemplateView 

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