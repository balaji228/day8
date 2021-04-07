from Emp.models import UsrRg
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username","required":True}),"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter password","required":True}),"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email id","required":True})}