from django.urls import path
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)

urlpatterns = [
    # Registration
    # auth
    path("auth/login", LoginView.as_view(), name="rest_login"),
    path("auth/logout/", LogoutView.as_view(), name="rest_logout"),
    # reset password
    path(
        "auth/password/reset/",
        PasswordResetView.as_view(),
        name="rest_password_reset",
    ),
    path(
        "auth/password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    # path(
    #     "auth/password/reset/confirm/<uidb64>/<token>/",
    #     view for frontend application where the user will be landed to reset the password,
    #     name="password_reset_confirm", # keep tha name
    # ),
    # change password
    path(
        "auth/password/change/",
        PasswordChangeView.as_view(),
        name="rest_password_change",
    ),
]
