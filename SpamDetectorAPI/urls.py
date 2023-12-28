from django.urls import path
from . import views


urlpatterns = [
    path('users', views.UsersList.as_view()),
    path('users/<str:pk>', views.UserDetail.as_view()),
    path('contacts', views.ContactsList.as_view()),
    path('user-contacts/<str:pk>', views.UserContactsList.as_view()),
]
