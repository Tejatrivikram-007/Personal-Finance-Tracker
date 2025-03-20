from django import forms
from .models import Income, Expense,Savings

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date','description']
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
            'date': forms.DateInput(attrs={'placeholder': 'Select date', 'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter a brief description'}),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description','date']
        widgets = {                                                                                                    #to add place holder
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter a brief description'}),
            'date': forms.DateInput(attrs={'placeholder': 'Select date', 'type': 'date'}),
        }

class SavingsForm(forms.ModelForm):
    class Meta:
        model = Savings
        fields = ['category', 'amount', 'description','date']
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter a brief description'}),
            'date': forms.DateInput(attrs={'placeholder': 'Select date', 'type': 'date'}),
        }

