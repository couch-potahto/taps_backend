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
			spouses.extend(children)
			qualified_members = FamilyMemberSerializer(spouses, many=True, read_only=True)
			house_data = {
				'housing_type': house.get_housing_type_display(),
				'qualified_members': qualified_members.data
			}
			response_data['family_togetherness_scheme'].append(house_data)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def elder_bonus(household_iter):
	response_data = {'elder_bonus':[]}
	household_iter = list(filter(lambda x: len(x.age_more_than(50))>0, household_iter))
	print(household_iter)
	for house in household_iter:
		qualified_members = FamilyMemberSerializer(house.age_more_than(50), many=True, read_only=True)
		house_data = {
			'housing_type': house.get_housing_type_display(),
			'qualified_members': qualified_members.data,
		}
		response_data['elder_bonus'].append(house_data)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def baby_sunshine_grant(household_iter):
	response_data = {'baby_sunshine_grant':[]}
	household_iter = list(filter(lambda x: len(x.age_less_than(5))>0, household_iter))
	for house in household_iter:
		qualified_members = FamilyMemberSerializer(house.age_less_than(5), many=True, read_only=True)
		house_data = {
			'housing_type': house.get_housing_type_display(),
			'qualified_members': qualified_members.data,
		}
		response_data['baby_sunshine_grant'].append(house_data)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def yolo_gst_grant(household_iter):
	response_data = {'yolo_gst_grant': []}
	household_iter = list(filter(lambda x: x.get_total_income() < 100000, household_iter))
	for house in household_iter:
		qualified_members = FamilyMemberSerializer(house.family_members.all(), many=True, read_only=True)
		house_data = {
			'housing_type': house.get_housing_type_display(),
			'qualified_members': qualified_members.data,
		}
		response_data['yolo_gst_grant'].append(house_data)
	return HttpResponse(json.dumps(response_data), content_type="application/json")
