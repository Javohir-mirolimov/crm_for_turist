from django.urls import path
from .views import *
urlpatterns = [
    path('create-user/', singup_view),
    path('login-user/', signin_view),
    path('logout-user/', logout_view),
    path('edit-user/<int:pk>/', edit_user_view),
    path('delete-user/<int:pk>/', delete_user),
    path('my-profile/', my_profile),
]