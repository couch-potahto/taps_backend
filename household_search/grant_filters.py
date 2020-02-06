'''
Contains functions that will filter a queryset based on grant requirements
'''
import json

from django.http import HttpResponse
from .serializers import *

def student_encouragement_bonus(household_iter):
	print('HERE')

	response_data = {'student_encouragement_bonus':[]}
	print(household_iter)
	household_iter = list(filter(lambda x: x.get_total_income() < 150000, household_iter))
	print(household_iter)
	for house in household_iter:
		if len(house.age_less_than(16)) > 0:
			qualified_members = FamilyMemberSerializer(house.age_less_than(16), many=True, read_only=True)
			house_data = {
			'housing_type': house.housing_type,
			'qualified_members': qualified_members.data
			}
			response_data['student_encouragement_bonus'].append(house_data)
	return HttpResponse(json.dumps(response_data), content_type="application/json")
