from django.urls import path,include
from .views import RegisterAPIView, AuthView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("auth/", AuthView.as_view()),
]