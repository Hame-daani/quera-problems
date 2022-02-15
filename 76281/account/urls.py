from django.urls import path

from .views import signup, joinoradd_team, login_account, logout_account, exit_team

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('team/', joinoradd_team, name='team'),
    path('logout/', logout_account, name='logout'),
    path('login/', login_account, name='login'),
    path('exit_team/', exit_team, name='exit')
]
