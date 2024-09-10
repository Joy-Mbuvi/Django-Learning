from django import forms

OPTIONS=[
     ('1', 'Pink'),
     ('2','Blue'),
     ('3','Yellow')
]

class CreateNewList(forms.Form):
    name=forms.CharField(label="Name",max_length=300)
    check=forms.BooleanField()
    age=forms.IntegerField()
    email=forms.EmailField(label='email address')
    birthdate=forms.DateField(widget=forms.SelectDateWidget(years=range(1980,2025)))
    password=forms.CharField(widget=forms.PasswordInput,label='Password')
    colours=forms.ChoiceField(choices=OPTIONS,label='pick color scheme')