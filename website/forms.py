from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Prob5_The_Anikanik_Girls

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	gc_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"GC name", "class":"form-control"}), label="")
	favorite_collectible = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Favorite Collectible", "class":"form-control"}), label="")
	favorite_collection = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Favorite Collection", "class":"form-control"}), label="")
	hacipupu_owned = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hacipupu Owned", "class":"form-control"}), label="")
	zsiga_owned = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zsiga Owned", "class":"form-control"}), label="")
	hirono_owned = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hirono Owned", "class":"form-control"}), label="")
	monthly_expense_on_collectible = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Monthly Expense on Collectible", "class":"form-control"}), label="")
	class Meta:
		model = Prob5_the_anikanik_girls
		exclude = ("user",)