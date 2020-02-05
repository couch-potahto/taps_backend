from django.urls import path
from .views import *

urlpatterns = [
    path('household/', HouseholdList.as_view()),
    path('household/<int:pk>/', HouseholdDetail.as_view()),
    path('household/<int:pk>/member/<int:member_id>/', HouseholdDetail.as_view()),
]
