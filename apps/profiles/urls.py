from django.urls import path, include
from apps.profiles.views import ProfileViewSet, MyProfileListView, ProfileFollowView
from rest_framework.routers import DefaultRouter

app_name = "profile"

router = DefaultRouter()
router.register("", ProfileViewSet)

urlpatterns=[
    path("me/", MyProfileListView.as_view(), name="myprofile"),
    path('<int:account_id>/follow/', ProfileFollowView.as_view(), name='follow-user'),
    path("",include(router.urls)),
]
