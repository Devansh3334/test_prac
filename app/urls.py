from django.urls import path
from .views import UserCreateView, login, MyProfileView,UserListView

urlpatterns= [
    path("user_create", UserCreateView.as_view(), name="user_create"),
    path('login/', login),
    path('myprofile/', MyProfileView, name='myprofile'),
    path('UserList/', UserListView.as_view(), name='UserList'),

]