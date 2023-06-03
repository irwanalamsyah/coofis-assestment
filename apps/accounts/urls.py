from django.urls import include, path
from apps.accounts.views import auth_views, user_views

app_name = "accounts"
urlpatterns = [
    path(
        "auth/",
        include(
            [
                path("login/", auth_views.LoginGenericAPIView.as_view(), name="auth-login"),
                path("refresh/", auth_views.RefreshGenericAPIView.as_view(), name="auth-refresh"),
                path("logout/", auth_views.LogoutGenericAPIView.as_view(), name="auth-logout"),
            ]
        ),
    ),
    path("user/",include([
        path("", user_views.UserRetrieveAPIView.as_view(), name="user-retrieve"),
    ]))
]