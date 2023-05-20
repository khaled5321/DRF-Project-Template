from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/v1/auth/login/", LoginView.as_view(), name="rest_login"),
    path("api/v1/auth/logout/", LogoutView.as_view(), name="rest_logout"),
    path(
        "api/v1/auth/password/reset/",
        PasswordResetView.as_view(),
        name="rest_password_reset",
    ),
    path(
        "api/v1/auth/password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path(
        "api/v1/auth/password/change/",
        PasswordChangeView.as_view(),
        name="rest_password_change",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
