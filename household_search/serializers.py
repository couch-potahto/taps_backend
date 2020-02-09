from rest_framework import serializers
from .models import *

class FamilyMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = FamilyMember
		fields = "__all__"


class ShowFamilyMemberSerializer(FamilyMemberSerializer):
	gender = serializers.CharField(source='get_gender_display')
	marital_status = serializers.CharField(source='get_marital_status_display')
	occupation_type = serializers.CharField(source='get_occupation_type_display')
	class Meta:
		model = FamilyMember
		exclude = ['household']

class HouseholdSerializer(serializers.ModelSerializer):
	class Meta:
		model = Household
		fields = "__all__"

class HouseholdDisplaySerializer(serializers.ModelSerializer):

	family_members = ShowFamilyMemberSerializer(many=True)
	housing_type = serializers.CharField(source='get_housing_type_display')

	class Meta:
		model = Household
		fields = ('housing_type', 'family_members')

class ShowHouseholdSerializer(HouseholdSerializer):
	family_members = ShowFamilyMemberSerializer(many=True, read_only=True)
	housing_type = serializers.CharField(source='get_housing_type_display')
