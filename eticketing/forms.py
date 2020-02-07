from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = {
    ('stripe', 'Stripe'),
    ('visa', 'Visa')
}


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'numéro et rue',
        'class': 'form-control'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Appartement, porte, bâtiment',
        'class': 'form-control'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    country = CountryField(blank_label='Choisir un pays').formfield(widget=CountrySelectWidget(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-control'
    }))
    save_info = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-control'
    }))
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
