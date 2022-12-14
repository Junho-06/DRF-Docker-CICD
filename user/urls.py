from django.urls import path,include
from .views import RegisterAPIView
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register('user', RegisterAPIView, basename='user')

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterAPIView.as_view()),
]