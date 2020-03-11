from django.urls import path
from .views import *

app_name = 'webApp'

urlpatterns = [
    path('utterance/', utterance),
    path('utterance1/', utterance1),
    path('kr/save/', saveKRMainAction),
    path('kr/read/', readKRMainAction),
    path('chartjs/', chartjs, name='chartjs'),
]
