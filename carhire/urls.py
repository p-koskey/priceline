from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Your URLs...
    path('api/profile/<id>', views.ProfileView.as_view(), name="profile"),
    path('api/userprofiles', views.ProfilesView.as_view(), name="userprofiles"),
    path('api/profile',views.ProfileIdView.as_view(), name="userprofile"),
    path('api/updateprofile',views.UpdateProfileView.as_view(), name="updateprofile"),
    path('api/Bookings/', views.BookingsList.as_view()),
    path('api/Bookings/<int:pk>/', views.BookingDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)


