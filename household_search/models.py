from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Household(models.Model):

	class HousingType(models.IntegerChoices):
		HDB = 1, _('HDB')
		LANDED = 2, _('Landed')
		CONDOMINIUM = 3, _('Condominium')

	housing_type = models.IntegerField(
		choices=HousingType.choices,
		null=False,
		blank=False
	)

	def get_household_size(self):
		return self.family_members.all().count()

	def get_total_income(self):
		return sum(member.annual_income for member in self.family_members.all())

	def age_less_than(self, age_limit): #returns list of people less than or equal to an age limit
		print('THERE')
		print(self.family_members.all())
		return list(filter(lambda x:
			date.today().year - x.date_of_birth.year - ((date.today().month, date.today().day) < (x.date_of_birth.month, x.date_of_birth.day)) <= age_limit,
			self.family_members.all()
			))

	def age_more_than(self, age_limit): #returns list of people more than or equal to an age limit
		return list(filter(lambda x:
			date.today().year - x.date_of_birth.year - ((data.today().month, data.today().day) < (x.date_of_birth.month, x.date_of_birth.day)) >= age_limit,
			self.family_members.all()
			))

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
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)


