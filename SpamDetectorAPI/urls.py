from django.urls import path
from . import views


urlpatterns = [
    path('users', views.user_view),
    path('users/<str:pk>', views.single_user_view),
]
