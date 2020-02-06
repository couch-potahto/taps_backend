from rest_framework import serializers
from .models import *

class FamilyMemberSerializer(serializers.ModelSerializer):
	gender = serializers.CharField(source='get_gender_display')
	marital_status = serializers.CharField(source='get_marital_status_display')
	occupation_type = serializers.CharField(source='get_occupation_type_display')
	class Meta:
		model = FamilyMember
		exclude = ['household',]

class ShowFamilyMemberSerializer(FamilyMemberSerializer):
	class Meta:
		model = FamilyMember
		exclude = ['spouse', 'household']

class HouseholdSerializer(serializers.ModelSerializer):
	family_members = FamilyMemberSerializer(many=True)
	housing_type = serializers.CharField(source='get_housing_type_display')
	class Meta:
		model = Household
		fields = ('housing_type', 'family_members')


class ShowHouseholdSerializer(HouseholdSerializer):
	family_members = ShowFamilyMemberSerializer(many=True, read_only=True)
