from django.shortcuts import render
from .models import Profile

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    return render(request, 'users/profiles.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    skills = profile.skill_set.all()
    context = {'profile': profile, 'skills': skills}
    return render(request, 'users/profile.html', context )
