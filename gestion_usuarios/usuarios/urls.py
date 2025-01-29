from django.urls import path
from .views import login_view, register_view, user_list, edit_user

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('users/', user_list, name='user_list'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
]
