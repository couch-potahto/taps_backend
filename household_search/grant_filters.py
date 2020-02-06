'''
Contains functions that will filter a queryset based on grant requirements
'''
import json

from django.http import HttpResponse
from .serializers import *

def student_encouragement_bonus(household_iter):
	response_data = {'student_encouragement_bonus':[]}
	household_iter = list(filter(lambda x: x.get_total_income() < 150000, household_iter))
	for house in household_iter:
		if len(house.age_less_than(16)) > 0:
			qualified_members = FamilyMemberSerializer(house.age_less_than(16), many=True, read_only=True)
			house_data = {
			'housing_type': house.get_housing_type_display(),
			'qualified_members': qualified_members.data
			}
			response_data['student_encouragement_bonus'].append(house_data)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def family_togetherness_scheme(household_iter):
	response_data = {'family_togetherness_scheme':[]}
	for house in household_iter:
		spouses = house.get_spouse()
		children = house.age_less_than(18)
		if len(spouses) == 2 and len(children) > 0:
			qualified_spouses = FamilyMemberSerializer(spouses, many=True, read_only=True)
			qualified_children = FamilyMemberSerializer(children, many=True, read_only=True)
			qualified_spouses.extend(qualified_children)
			house_data = {
			'housing_type': house.get_housing_type_display(),
			'qualified_members': qualified_spouses.data
			}
			response_data['family_togetherness_scheme'].append(house_data)
	return HttpResponse(json.dumps(response_data), content_type="application/json")
