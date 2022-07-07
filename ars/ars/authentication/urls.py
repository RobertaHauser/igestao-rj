from django.conf import settings

from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name=settings.LOGIN_URL),
    path('logout/', auth_views.LogoutView.as_view(), name=settings.LOGOUT_URL),
    path('edit-account/<int:pk>/', views.EditAccountView.as_view(), name='edit_account'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
