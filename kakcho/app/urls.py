from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

urlpatterns= [
        path("login/", views.LoginView.as_view(), name="login"),
        path("logout/", auth_views.LogoutView.as_view(), name="logout"),
        path("social_auth/", include('social_django.urls', namespace="social")),
        path('home/', TemplateView.as_view(template_name='home.html'), name="home"),
        path("upload/", views.UploadView.as_view(), name="upload"),
        path("task1/<int:pk>/", views.FirstTaskView.as_view(), name= "task1"),
        path("task2/<int:pk>/", views.SecondTaskView.as_view(), name="task2"),
        path("roundoff/<int:pk>/", views.RoundOffView.as_view(), name="roundoff"),
        ]
