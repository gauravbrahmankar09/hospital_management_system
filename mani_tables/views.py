from django.shortcuts import render
from django.db import connection 
from django.http import HttpResponse , HttpResponseRedirect
from forms import TestForm , PatientForm , DepartmentForm , DoctorForm
from django.template import Context, Template
from general import dictfetchall
#-------------------------------home---------------------------------
def home(request) :
	template = 'mani_tables/carousel-home.html'
	return render(request , template , {} )
#--------------------------generic-views-----------------------------
def show(request , tablename) :
	c = connection.cursor()
	c.execute('select * from %s' %(tablename) )
	[ rows , cols ]  = dictfetchall(c)
	template = 'mani_tables/show_tables.html'
	context = { 'table' : tablename , 'columns' : cols , 'rows' : rows }
	c.close()
	return render(request, template , context)
def profile_list (request , tablename) :
	template = 'mani_tables/profile-list.html'
	c = connection.cursor()
	c.execute('select * from %s' %(tablename) )
	[ rows , cols ]  = dictfetchall(c)
	return render(request , template , {'table' : tablename , 'tableinfo' : rows} )
	
#---------------------------empty-forms-----------------------------
def render_forms (request) : 
	patient = PatientForm ()
	department = DepartmentForm()
	doctor = DoctorForm()
	return render(request, 'mani_tables/all_forms.html', {'patient': patient , 'department' : department , 'doctor' : doctor})
#---------------------------------------------------------------------

#========================================== FUNDAMENTAL TABLES-VIEW PROCESSING =======================================================================    
#----------------------------Patient----------------------------------

def insert_into_patient(request) :
	if request.method == 'POST' :
		form = PatientForm(request.POST)
		if form.is_valid() :
			c = connection.cursor()
			ID =  form.cleaned_data['ID']
			name = form.cleaned_data['name']
			age = form.cleaned_data['age']
			sex = form.cleaned_data['sex']	
			BP = form.cleaned_data['BP']
			height = form.cleaned_data['height']
			weight = form.cleaned_data['weight']
			address = form.cleaned_data['address']
			contact = form.cleaned_data['contact']
			condition = form.cleaned_data['condition']
			admitted = form.cleaned_data['admitted']
			fee = form.cleaned_data['fee']
			c.execute("insert into patient VALUES(%s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s)" , [ID , name , age , sex , BP, height, weight, address , contact , condition , admitted , fee])
			c.close()
	return HttpResponseRedirect("/mani_tables/show_patient")
#----------------------------Department-------------------------------
def insert_into_department(request) :
	if request.method == 'POST' :
		form = DepartmentForm(request.POST) 
		if form.is_valid() :
			c = connection.cursor() 
			dept_name = form.cleaned_data['dept_name']
			HOD = form.cleaned_data['HOD']
			floor_no = form.cleaned_data['floor_no']		
			c.execute("insert into department VALUES(%s , %s , %s )" , [dept_name , HOD , floor_no])
			c.close()
	return HttpResponseRedirect("/mani_tables/show_department")
#---------------------------Doctor--------------------------------------
def insert_into_doctor(request) :
	if request.method == 'POST' :
		form = DoctorForm(request.POST) 
		if form.is_valid() :
			c = connection.cursor()
			ID = form.cleaned_data['ID']
			name = form.cleaned_data['name']
			age = form.cleaned_data['age']
			sex = form.cleaned_data['sex']
			salary = form.cleaned_data['salary'] 
			specialisation = form.cleaned_data['specialisation']
			experience = form.cleaned_data['experience']
			position = form.cleaned_data['position']
			c.execute("insert into doctor VALUES (%s , %s , %s , %s , %s , %s , %s , %s ) " , [ID , name, age , sex , salary , specialisation , experience , position ])
			c.close()
	return HttpResponseRedirect("/mani_tables/show_doctor")	
#---------------------------test--------------------------------extraneous--------
def insert_into_test (request) :
	if request.method == 'POST' :
		form = TestForm(request.POST)
		if form.is_valid() :
			c = connection.cursor()
			c.execute("insert into test VALUES(%s , %s)" , [form.cleaned_data['name'] , form.cleaned_data['cost']])
			c.close()
			
	else :
		form = TestForm ()
	
	return render(request, 'mani_tables/test_entry_form.html', {'form': form})


## AKASH'S ADDED FUNCTIONS
def give_patient_profile(request, pat_id):
	# search what all services have been availed by the patient, what is his total fee.			
	patient_id = request.ID
	c = connection.cursor()

	patient = h.Patient()
	patient.get_info(patient_ID)
	patient.calculate_fee()

## somehow display the information here.
	# complete info in the patient object.
	return render(request, 'mani_tables/patient_profiles.html', {'patient':patient}) # sending a patient object contaning full info of the patient

def give_profiles(request, tablename, ent_id):
	c = connection.cursor()
	c.execute("select * from %s where id = %s" % (tablename, ent_id))S
	c = connection.cursor()
	c.execute("update %s set paid = 'True'" % tablename)
	
def pay_entity(request, tablename):
	c = connection.cursor()
	c.execute("update %s set paid = 'True'" % tablename)
