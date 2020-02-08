# TAPS 6 Technical Assignment (Backend)
 
## Installation Guide
First, clone this repository into your local machine
Next, ensure that you have Python 3 and pip3 installed.
```bash
sudo apt-get update 
sudo apt-get install python3.7
sudo apt install python3-pip
```
Then, install Django and Django Rest Framework with the following commands:

```bash
pip3 install django
pip3 install djangorestframework
```

Sample Household and Family Members object have already been created in the sqlite3 database. 
In order to set up the database, first ```cd taps_backend```, then run the following command:

```python
python3 manage.py migrate
```

After the migration is completed, the server can be fired up with the following command:

```python
python3 manage.py runserver
```

The server can be accessed via ```http://127.0.0.1:8000```.

## API Reference

This section serves to summarize the endpoints for the various actions implemented.
1) Create Household: ```POST http://127.0.0.1:8000/api/household/ housing_type=x```, where x is an integer that can be 1 = HDB, 2 = LANDED, 3 = CONDOMINIUM

2) Add Family Member to Household: ```POST http://127.0.0.1:8000/api/household/<house_pk>/member/<member_pk>```, where member_pk is the primary key of the Family Member instance you wish to add to Household instance of primary key house_pk

3) List Households: ```GET http://127.0.0.1:8000/api/household/```

4) Show Household: ```GET http://127.0.0.1:8000/api/household/<house_pk>``` , which will show the housing type and Family Member instances, if any, in household instance of primary key house_pk

5) Search for households and recipients of grant disbursement endpoint: 
```GET http://127.0.0.1:8000/api/household/grant=<grant_name>```, which will retrieve a list of all households that qualify for the specified grant regardless of income ceiling or household size

```GET http://127.0.0.1:8000/api/household/grant=<grant_name>/income=<income_ceiling>```, which will retrieve a list of all households below a total annual income of specified <income ceiling> that qualify for the specified grant
 
```GET http://127.0.0.1:8000/api/household/grant=<grant_name>/size=<household_size>```, which will retrieve a list of all households of size <household_size> that qualify for the specified grant 

```GET http://127.0.0.1:8000/api/household/grant=<grant_name>/income=<income_ceiling>/size=<household_size>```, which will retrieve a list of all households of size <household_size> below a total annual income of specified <income_ceiling> that qualify for the specified grant 

income and size are optional parameters that can be passed when the need arises, and must follow the aforementioned format.

6) Delete Household: ```DELETE http://127.0.0.1:8000/api/household/<house_pk>```, which will delete household of primary key <house_pk>

7) Delete Family Member ```DELETE http://127.0.0.1:8000/api/household/<house_pk>/member/<member_pk>```, which will remove family member of primary key <member_pk> from household of primary key <house_pk>

## Assumptions for Grant Results
1) Only family members taken into account for grant eligibility will be shown alongside the household.
2) The optional ```income``` parameter refers to an income ceiling, i.e. only households under a certain total annual income as specified by the ```income``` parameter will be considered and listed out
