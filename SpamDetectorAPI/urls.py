from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views



urlpatterns = [
    path('auth-token', obtain_auth_token),
    
    path('register', views.RegisterUser.as_view()),
    path('users', views.ListUsers.as_view()),
    # path('users/<str:pk>', views.UserDetail.as_view()),
    # path('contacts', views.ContactsList.as_view()),
    # path('user-contacts/<str:pk>', views.UserContactsList.as_view()),
    
]
