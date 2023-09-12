from django import forms

g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('django','DNAGO'),('api','API'),('sql','SQL'),('selenium','SELENIUM')]
class RegistrationForm(forms.Form):
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    Gender=forms.ChoiceField(choices=g)
    Gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    # Courses=forms.MultipleChoiceField(choices=c)
    Courser=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
