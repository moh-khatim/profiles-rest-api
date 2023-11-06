from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiles', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('',include(router.urls))
]