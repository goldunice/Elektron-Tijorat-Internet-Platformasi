from django.urls import path
from .views import *

urlpatterns = [
    path('tanlangan_qosh/<int:pk>/', TanlanganlargaQoshView.as_view()),
    path('tanlanganlar/', TanlanganlarView.as_view()),
    path('buyurtmalar/', BuyurtmalarView.as_view()),
    path('savat/', SavatlarView.as_view()),
    path('t_ochir/<int:pk>/', DeleteTanlanganItem.as_view()),
    path('s_i_ochir/<int:pk>/', DeleteSavatItem.as_view()),
    path('add_savatitem/<int:pk>/', AddSavatItemView.as_view()),
    path('miqdor_q/<int:pk>/', MiqdorQosh.as_view()),
    path('miqdor_k/<int:pk>/', MiqdorKamaytir.as_view()),
    path('add_savatitem/<int:pk>/', AddSavatItemView.as_view()),
    path('buyurtma_qosh/', BuyurtmaQosh.as_view())
]
