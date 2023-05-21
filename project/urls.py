from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    # Redirect to docs page
    path("", lambda req: redirect("/api/v1/docs/")),
    # Admin page
    path("admin/", admin.site.urls),
    # Docs
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    # confirm email view
    # path(
    #     "api/v1/registration/account-confirm-email/<key>/",
    #     custom view,
    #     name="account_confirm_email",
    # ),
    # reset password
    # path(
    #     "auth/password/reset/confirm/<uidb64>/<token>/",
    #     custom view,
    #     name="password_reset_confirm", # keep tha name
    # ),
    # dj-rest-auth
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/registration/", include("dj_rest_auth.registration.urls")),
    # My apps
    path("api/v1/", include("users.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
