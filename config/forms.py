from django import forms


class QRCodeForm(forms.Form):
  name = forms.CharField(
    max_length=50,
    label='Business',
    widget=forms.TextInput(attrs={
       'class': 'form-control',
       'placeholder': 'Enter name'
    }),
    )
  url = forms.URLField(
    max_length=200, 
    label= 'URL',
    widget= forms.URLInput(attrs={
      'class': 'form-control',
      'placeholder': 'Enter the URL of your site'
    }),
    )