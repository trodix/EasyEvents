from django import forms


class CustomerForm(forms.Form):
    lastname = forms.CharField(label='Nom', max_length=100, label_suffix='',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    firstname = forms.CharField(label='Prénom', max_length=100, label_suffix='',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Email', max_length=100, label_suffix='',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    billing_address = forms.CharField(label='Adresse', max_length=100, label_suffix='',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))

    billing_zipcode = forms.CharField(label='Code postal', max_length=5, label_suffix='',
                                      widget=forms.NumberInput(attrs={'class': 'form-control'}))

    billing_city = forms.CharField(label='Ville', max_length=100, label_suffix='',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    billing_country = forms.CharField(label='Pays', max_length=100, label_suffix='',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
