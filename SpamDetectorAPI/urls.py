from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    #JWT routes
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('register', views.RegisterUser.as_view()),
    path('users', views.ListUsers.as_view()),
    # path('users/<str:pk>', views.UserDetail.as_view()),
    # path('contacts', views.ContactsList.as_view()),
    # path('user-contacts/<str:pk>', views.UserContactsList.as_view()),
    
]
