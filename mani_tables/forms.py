from django import forms

class TestForm(forms.Form) :
	name = forms.CharField(label='name', max_length=100)
	cost = forms.IntegerField(label = 'cost')
	
class PatientForm(forms.Form) :
	ID = forms.CharField(label = 'id'  ,  widget=forms.TextInput(attrs={'placeholder': "Patient's Id" , 'class' : 'form-control'}) )
	name  = forms.CharField(label = 'name', widget=forms.TextInput(attrs={'placeholder': 'Name' , 'class' : 'form-control'}))
	age = forms.IntegerField(label = 'age' , widget=forms.TextInput(attrs={'placeholder': 'Age' , 'class' : 'form-control'}) ) 
	sex = forms.ChoiceField( label = 'sex' , choices=(('Male','Male'), ('Female' , 'Female')),  widget=forms.RadioSelect )
	BP = forms.CharField(label = 'bp', widget=forms.TextInput(attrs={'placeholder' : 'Blood Pressure' , 'class' : 'form-control'} ))
	height = forms.IntegerField(label ='height', widget=forms.TextInput(attrs={'placeholder' : 'Height' , 'class' : 'form-control'} ))
	weight = forms.IntegerField(label ='weight', widget=forms.TextInput(attrs={'placeholder' : 'Weight' , 'class' : 'form-control'} ))
	address = forms.CharField(label ='address', widget=forms.TextInput(attrs={'placeholder' : 'Address' , 'class' : 'form-control'} ))
	contact = forms.CharField(label = 'contact', widget=forms.TextInput(attrs={'placeholder' : 'Contact Information' , 'class' : 'form-control'}  ))
	condition = forms.ChoiceField( label = 'condition' , choices = (('Critical','Critical') , ('Not Critical','Not Critical')) , widget=forms.RadioSelect)
	admitted = forms.ChoiceField(label= 'admitted' , choices = (('True','True') , ('False','False')) , widget=forms.RadioSelect )
	fee = forms.IntegerField(label = 'fee', widget=forms.TextInput(attrs={'placeholder' : 'Fee' , 'class' : 'form-control'}  ))


class DepartmentForm(forms.Form) :
	dept_name = forms.CharField(label = 'id'  ,  widget=forms.TextInput(attrs={'placeholder': "Department Name" , 'class' : 'form-control'}) )
	HOD = forms.CharField(label = 'id'  ,  widget=forms.TextInput(attrs={'placeholder': "Head Of Department" , 'class' : 'form-control'}) )
	floor_no = forms.CharField(label = 'id'  ,  widget=forms.TextInput(attrs={'placeholder': "Floor Number" , 'class' : 'form-control'}) )
	
class DoctorForm(forms.Form) :
	ID = forms.CharField(label = 'id'  ,  widget=forms.TextInput(attrs={'placeholder': "ID" , 'class' : 'form-control'}) )
	name = forms.CharField(label = 'name'  ,  widget=forms.TextInput(attrs={'placeholder': "Doctor's Name" , 'class' : 'form-control'}) )
	age = forms.IntegerField(label = 'age' , widget=forms.TextInput(attrs={'placeholder': 'Age' , 'class' : 'form-control'}) ) 
	sex = forms.ChoiceField( label = 'sex' , choices=(('Male','Male'), ('Female' , 'Female')),  widget=forms.RadioSelect )
	salary = forms.IntegerField(label = 'salary' , widget=forms.TextInput(attrs={'placeholder': "Doctor's Salary" , 'class' : 'form-control'}) ) 
	specialisation = forms.CharField(label = 'specialisation'  ,  widget=forms.TextInput(attrs={'placeholder': "Speciality" , 'class' : 'form-control'}) ) 
	experience = forms.IntegerField(label = 'experience' , widget=forms.TextInput(attrs={'placeholder': 'Years of Experience' , 'class' : 'form-control'}) ) 
	position = forms.ChoiceField( label = 'position' , choices=(('Junior Doctor','Junior Doctor'), ('Senior Doctor','Senior Doctor')),  widget=forms.RadioSelect )


