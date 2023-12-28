from django.urls import path
from . import views


urlpatterns = [
    path('users', views.UsersView.as_view()),
    path('users/<str:pk>', views.SingleUserView.as_view()),
]
