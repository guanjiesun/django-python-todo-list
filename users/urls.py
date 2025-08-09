from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url='/users/password-change-done/'
        ),
        name='password_change'
    ),
    path(
        'password-change-done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
        ),
        name='password_change_done'
    ),
    path('get-session/', views.get_session, name='get_session'),
    # path('show-messages/', views.show_messages, name='show_messages'),
    # path('test-messages/', views.test_messages, name='test_messages'),
]
