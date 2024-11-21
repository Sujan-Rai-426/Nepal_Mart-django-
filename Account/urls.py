

# Manually created file

from django.urls import path
from Account import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('registration/', views.Register_User_View, name='register_user'),
    path('login/', views.Login_User_View, name='login_user'),
    path('logout/', views.Logout_User_View, name='logout_user'),

]