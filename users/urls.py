from django.urls import path
from .import views
from .models import Profile
urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('user-profile/<str:pk>', views.profile, name="profile")
]

print(Profile.name)
