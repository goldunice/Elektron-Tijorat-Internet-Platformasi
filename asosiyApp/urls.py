from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('bolimlar/', BolimlarView.as_view()),
    path('bolim/<int:id>/', MahsulotlarView.as_view()),
    path('mahsulot/<int:id>/', MahsulotView.as_view()),
]
