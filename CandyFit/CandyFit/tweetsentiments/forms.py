from django import forms

class Candiate_Form(forms.Form):
    Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    Email = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    Phone_Number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    Job_Title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Job Title'}))
    Cover_Title = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Cover Letter'}))
    Extra_Curricular = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Extra-Curricular'}))
    Social_Profile = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'LinkedIn Profile'}))
    # Resume = forms.FileField(label='Select a file',help_text='max. 42 megabytes')

class Company_Form(forms.Form):
    Company_id = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Company Id'}))
    Description = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'About us'}))
    Job_Title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Job Title'}))
    Company_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    Perks = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Perks'}))
    Activities = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Activities'}))
    # Resume = forms.FileField(label='Select a file',help_text='max. 42 megabytes')

class Analyse_Form(forms.Form):
    Company_id = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Company Id'}))
    Job_Title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Job Title'}))
