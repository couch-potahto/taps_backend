from django.db import models

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
	housing_type = models.IntegerField(choices=HOUSING_TYPES)

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

	name = models.CharField(max_length=255):
	gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
	marital_status = models.IntegerField(choices=MARITAL_STATUSES, default=SINGLE)
	spouse = models.OneToOneField(
		FamilyMember,
		on_delete=SET_NULL,
		null=True,
		blank=True,
	)
	occupation_type = models.IntegerField(choices=OCCUPATIONS, default=UNEMPLOYED)
	annual_income = models.PositiveIntegerField(default = 0)
	date_of_birth = models.DateField()



