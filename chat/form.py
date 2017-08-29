from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from models import Profile
from django.forms import ModelForm
from chat.models import Createclass

class SignUpForm(UserCreationForm):
    utype = forms.CharField(max_length=30, required=False,initial='3',widget=forms.HiddenInput(),label='')
    

    class Meta:
        model = User
        widgets = {
		    'first_name': forms.TextInput(attrs={'required':'required','class': 'form-control','placeholder':'Enter First Name'})
			,'last_name': forms.TextInput(attrs={'required':'required','class': 'form-control','placeholder':'Enter Last Name'})
	        ,'username': forms.TextInput(attrs={'required':'required','class': 'form-control','placeholder':'Enter Username'})
            ,'password1': forms.PasswordInput(attrs={'required':'required','class': 'form-control','placeholder':'Enter Password1'})
            ,'password2': forms.PasswordInput(attrs={'required':'required','class': 'form-control','placeholder':'Enter Password2'})
		    ,'email': forms.TextInput(attrs={'required':'required','class': 'form-control','placeholder':'Enter Email'})}
        fields = ('username','first_name','last_name','password1','password2','email')
			
		
#class Profile(forms.ModelForm):
 #   class Meta:
  #      model = Profile
   #     fields = ('utype')		
		 
def save(self, commit=True):
        user = Super(RegistrationForm, self).save(commit=False)
        user.profile.utype = self.cleaned_data['utype']

        if commit:
            user.save()

        return user	
	
class EditProfileform(UserChangeForm):
    utype = forms.CharField(max_length=30, required=False,widget=forms.HiddenInput())

    class Meta:
        model =User
        fields = {
		
		
		
		}
		
class ContactForm(forms.Form):
  subject = forms.CharField(widget=forms.TextInput(attrs={'size':'48', 'class':'form-control'}))
 # email_to = forms.MultipleChoiceField(widget=forms.SelectMultiple,
  #                                           choices=OPTIONS_TUPPLE)
 # message = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5 , 'class':'form-control'}))
		
