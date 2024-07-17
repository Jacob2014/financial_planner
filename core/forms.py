from django import forms
from .models import Income, Expense
from bootstrap_datepicker_plus.widgets import DatePickerInput

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'amount', 'source']
        widgets = {
            'date': DatePickerInput().start_of('event days')
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'category']
        widgets = {
            'date': DatePickerInput().start_of('event days')
        }
