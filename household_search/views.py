from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

#@api_view(['GET', 'POST'])
class HouseholdList(APIView):

	def get(self, request, format=None):
		households = Household.objects.all()
		serializer = HouseholdSerializer(households, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = HouseholdSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HouseholdDetail(APIView):
	"""
	Retreive, update or delete a household instance
	"""
	def get_object(self, pk):
		try:
			return Household.objects.get(pk=pk)
		except Household.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		household = self.get_object(pk)
		serializer = HouseholdSerializer(household)
		return Response(serializer.data)

	def patch(self, request, pk, member_id, format=None):
		household = self.get_object(pk)
		new_member = FamilyMember.objects.get(pk=member_id)
		new_member.household = household
		new_member.save()
		serializer = HouseholdSerializer(household)
		print(serializer)
		return Response(serializer.data)
