from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('household/', HouseholdList.as_view()),
    path('household/<int:pk>/', HouseholdDetail.as_view()),
    path('household/<int:pk>/member/<int:member_id>/', EditHouseholdMembers.as_view()),
    path('household/grant=<slug:grant_type>/', include([
    	path('', HouseholdQueryList.as_view()),
    	path('income=<int:total_income>', HouseholdQueryList.as_view()),
    	path('size=<int:household_size>', HouseholdQueryList.as_view()),
    	path('income=<int:total_income>/size=<int:household_size>', HouseholdQueryList.as_view()),
    ]))
]
