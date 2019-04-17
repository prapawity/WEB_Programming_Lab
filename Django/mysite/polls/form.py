from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


def validate_even(value):
    if(value%2 != 0):
        raise ValidationError('%(value)s Not Even',params={'value':value})
class PollForm(forms.Form):
    title = forms.CharField(label="ชื่อโพล",max_length=100,required=True)
    email = forms.CharField(validators=[validators.validate_email])
    no_questions = forms.IntegerField(label="จำนวนคำถาม",min_value=0,max_value=10,required=True,validators=[validate_even])
    start_date = forms.DateField()
    end_date = forms.DateField()

    def clean_title(self):
        data = self.cleaned_data['title']
        if('ไอทีหมีแพนด้า') not in data:
            raise forms.ValidationError('You Forget Fac name')
        return data

    def clean(self):
        cleaned_data = super.clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        if start and not end:
            raise forms.ValidationError('Please input end')
        elif end and not start:
            raise forms.ValidationError('Please input start')