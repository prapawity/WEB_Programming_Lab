import datetime

from django import forms

from polls.models import Transaction


class TransactionForm(forms.ModelForm):
    create_by = forms.IntegerField(required=False, widget=forms.HiddenInput)
    approve_status = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'reason': forms.TextInput(attrs={'class': 'reason'}),
            'type': forms.Select()
        }

    def clean(self):
        current = datetime.date.today()
        clean_data = super().clean()

        start = clean_data.get('start_date')
        end = clean_data.get('end_date')
        text = clean_data.get('reason')
        if text == '':
            raise forms.ValidationError('กรุณากรอกข้อมูลให้ถูกต้อง')
        if start and not end:
            raise forms.ValidationError('โปรดเลือกวันที่สิ้นสุด')
        if not start and end:
            raise forms.ValidationError('โปรดเลือกวันที่เริ่มต้น')
        if (end < start):
            raise forms.ValidationError('กรุณาเลือกวันที่ให้ถูกต้อง')
        if(end < current or start < current):
            raise forms.ValidationError('กรุณาเลือกวันที่ให้ถูกต้อง')
