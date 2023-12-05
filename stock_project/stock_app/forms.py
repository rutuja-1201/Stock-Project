from django import forms

class StockForm(forms.Form):
    symbol = forms.CharField(max_length=10)