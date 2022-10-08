from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('account/', views.user_account, name='user_account'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    path('', include('django.contrib.auth.urls'))

]

