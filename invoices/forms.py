from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    completion_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    payment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Invoice
        fields = (
            'receiver',
            'number',
            'completion_date',
            'issue_date',
            'payment_date',
            )

        labels = {
            
        }

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if len(number)<10:
            raise forms.ValidationError('Number is too short')
        return number