"""sns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from api_user import views
from rest_framework.routers import DefaultRouter

app_name = "user"
router = DefaultRouter()
router.register("profile", views.ProfileViewSet)
router.register("approval", views.FriendRequestViewSet)

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("myprofile/", views.MyProfileListView.as_view(), name="myprofile"),
    path("", include(router.urls))
]
