from django.db import models
from datetime import date
# Create your models here.
class Household(models.Model):
	HDB = 1
	LANDED = 2
	CONDOMINIUM = 3
	HOUSING_TYPES = (
		(HDB, 'HDB'),
		(LANDED, 'Landed'),
		(CONDOMINIUM, 'Condominium'),
	)
	housing_type = models.IntegerField(
		choices=HOUSING_TYPES,
		null=False,
		blank=False
	)

	def get_household_size(self):
		return self.family_members.all().count()

	def get_total_income(self):
		return sum(member.annual_income for member in self.family_members.all())

	def age_less_than(self, age_limit): #returns list of people less than or equal to an age limit
		return list(filter(lambda x:
			date.today().year - x.date_of_birth.year - ((date.today().month, date.today().day) < (x.date_of_birth.month, x.date_of_birth.day)) <= age_limit,
			self.family_members.all()
		))

	def age_more_than(self, age_limit): #returns list of people more than or equal to an age limit
		return list(filter(lambda x:
			date.today().year - x.date_of_birth.year - ((date.today().month, date.today().day) < (x.date_of_birth.month, x.date_of_birth.day)) >= age_limit,
			self.family_members.all()
		))

	def get_spouse(self): #can have multiple pairs of married couples living together (Father, Mother and Son, Daughter-in-Law)
		are_married = list(filter(lambda x: x.marital_status == 3, self.family_members.all()))
		husband_and_wife = []

		for individual in are_married:
			if individual.spouse in are_married and individual.spouse not in husband_and_wife:
				husband_and_wife.append(individual)
				husband_and_wife.append(individual.spouse)
				break
		return husband_and_wife

class FamilyMember(models.Model):

	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	)

	SINGLE = 1
	ENGAGED = 2
	MARRIED = 3
	DIVORCED = 4
	MARITAL_STATUSES = (
		(SINGLE, 'Single'),
		(ENGAGED, 'Engaged'),
		(MARRIED, 'Married'),
		(DIVORCED, 'Divorced'),
	)

	UNEMPLOYED = 1
	STUDENT = 2
	EMPLOYED = 3
	OCCUPATIONS = (
		(UNEMPLOYED, 'Unemployed'),
		(STUDENT, 'Student'),
		(EMPLOYED, 'Employed'),
	)

	name = models.CharField(max_length=255)
	gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
	marital_status = models.IntegerField(choices=MARITAL_STATUSES, default=SINGLE)
	spouse = models.OneToOneField(
		'self',
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)
	occupation_type = models.IntegerField(choices=OCCUPATIONS, default=UNEMPLOYED)
	annual_income = models.PositiveIntegerField(default = 0)
	date_of_birth = models.DateField()
	household = models.ForeignKey(
		Household,
		related_name='family_members',
		on_delete=models.CASCADE,
		null=True,
		blank=True,
	)

	def __str__(self):
		return self.name + "pk:" + str(self.pk)

