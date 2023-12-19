from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('tasdiqlash/', KodTasdiqlash.as_view()),
]
