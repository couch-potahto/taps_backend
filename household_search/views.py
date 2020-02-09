from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .grant_filters import *
from django.http import HttpResponse, Http404

class HouseholdList(APIView):

	def get(self, request, format=None):
		households = Household.objects.all()
		serializer = HouseholdDisplaySerializer(households, many=True)
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
		try:
			household = self.get_object(pk)
		except Household.DoesNotExist:
			raise Http404
		serializer = ShowHouseholdSerializer(household)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		try:
			household = self.get_object(pk=pk)
		except Household.DoesNotExist:
			raise Http404
		household.delete()
		'''should not remove any family members
		'''
		return Response(status=status.HTTP_204_NO_CONTENT)

class EditHouseholdMembers(APIView):

	'''
	add or remove members from household
	'''

	def post(self, request, pk, format=None):
		try:
			household = Household.objects.get(pk=pk)
		except Household.DoesNotExist:
			raise Http404
		serializer = FamilyMemberSerializer(data=request.data)
		if serializer.is_valid():
			member = serializer.save()
			member.household = household
			member.save()
			if "spouse" in request.data:
				spouse_pk = int(request.data['spouse'])
				member_spouse = FamilyMember.objects.get(pk=spouse_pk)
				member_spouse.spouse = member
				member_spouse.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, member_id, format=None):
		try:
			member_to_remove = FamilyMember.objects.get(pk=member_id)
		except FamilyMember.DoesNotExist:
			raise Http404
		if member_to_remove.household.pk != pk:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			member_to_remove.delete()
			return Response(status=status.HTTP_200_OK)

class HouseholdQueryList(APIView):

	def get(self,request, grant_type, total_income=None, household_size=None, format=None):

		grants = {
		'student_encouragement_bonus': student_encouragement_bonus,
		'family_togetherness_scheme': family_togetherness_scheme,
		'elder_bonus': elder_bonus,
		'baby_sunshine_grant': baby_sunshine_grant,
		'yolo_gst_grant': yolo_gst_grant
		}

		queryset = Household.objects.all()
		serializer = HouseholdSerializer(queryset, many=True)
		grant_type = self.kwargs['grant_type']
		'''if no size given, give all'''
		if 'household_size' in self.kwargs:
			household_size = self.kwargs['household_size']
			queryset = list(filter(lambda x: x.get_household_size() == household_size, queryset))
		if 'total_income' in self.kwargs:
			total_income = self.kwargs['total_income']
			queryset = list(filter(lambda x: x.get_total_income() <= total_income, queryset))
		return grants[grant_type](queryset)
