from django.urls import path, include
from django.conf.urls.static import static
from auth_user.views import*

urlpatterns = [
    path('login', login_user,name='login'),
    path('signup', signup_user,name='signup'),
    path('logout', logout_user,name='logout'),
]