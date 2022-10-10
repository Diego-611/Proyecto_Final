from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('signup/', viewSignup, name='SignupUser'),
    path('login/', viewLogin, name= 'LoginUser'),
    path('logout/', LogoutView.as_view(template_name= 'AppUsuario/logoutUser.html' ), name='LogoutUser'),
    path('edit', viewEdit, name='Edit'),
    path('editusername/', viewEditUserName, name='EditUser'),
    path('editdescription/', viewEditDescription, name='EditDescription'),
    path('editlink/', viewEditLink, name='EditLink'),
    path('editavatar/', viewEditAvatar, name='EditAvatar'),
    path('profile/', viewProfile, name='Profile'),
    path('loginflash/', viewLoginFlash, name='LoginFlash'),
    path('uprofile/<id>', viewUProfile, name='UProfile'),
    path('delete/', viewDeleteUser, name='Delete')
]