from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Your URLs...
    path('api/profile/<id>', views.ProfileView.as_view(), name="profile"),
    path('api/userprofiles', views.ProfilesView.as_view(), name="userprofiles"),
    path('api/profile',views.ProfileIdView.as_view(), name="userprofile"),
    path('api/updateprofile',views.UpdateProfileView.as_view(), name="updateprofile"),
]