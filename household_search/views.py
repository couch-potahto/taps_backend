from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def household_list(request):

	if request.method == "GET":
		households = Household.objects.all()
		serializer = HouseholdSerializer(households, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = HouseholdSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
