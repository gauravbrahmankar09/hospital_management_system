from django.conf.urls import url

import views

urlpatterns = [
	#home-carousel
	url(r'^home$' , views.home , name = 'home'),
	
	#delete entry 
	url( r'^delete/(?P<tablename>[a-z]+)/(?P<pk>[a-z 0-9]+)/$'  , views.delete_on_pk , name = 'delete' ),

	#form-url
	url(r'^renderforms$' , views.render_forms , name = 'render_forms'),

	#patient-handler
    url(r'^show_patient$', views.show , {'tablename' : 'patient'} , name='show_patient' ),
	url(r'^insert_patient$' , views.insert_into_patient , name = 'insert_patient'),
	url(r'^patient_profile$' , views.profile_list , {'tablename' : 'patient'} , name = 'patient_profile_list'),
	
	#department-handler
	url(r'^show_department$' , views.show , {'tablename' : 'department'} , name = 'show_department'),
	url(r'^insert_department$' , views.insert_into_department , name = 'insert_department'),
	
	#doctor-handler 
	url(r'^show_doctor$' , views.show , {'tablename' : 'doctor'} , name = 'show_doctor'),
	url(r'^insert_doctor$' , views.insert_into_doctor , name = 'insert_doctor'),
	url(r'^doctor_profile$' , views.profile_list , {'tablename' : 'doctor'} , name = 'doctor_profile_list'),
		
]
