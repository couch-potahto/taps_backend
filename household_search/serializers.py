from rest_framework import serializers
from .models import *

class FamilyMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = FamilyMember
		fields = '__all__'

class HouseholdSerializer(serializers.ModelSerializer):
	family_members = FamilyMemberSerializer(many=True, read_only=True)
	housing_type = serializers.CharField(source='get_housing_type_display')
	class Meta:
		model = Household
		fields = ('housing_type', 'family_members')

