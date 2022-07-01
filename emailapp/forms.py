import email
from django import forms
from emailapp.models import EmailLog
import requests





class FormEmailAdd(forms.ModelForm):


    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email','placeholder':'Enter a valid email address.'}))
    class Meta:
        model = EmailLog
        fields =  '__all__'



    def disposable_checker(self):
            email  = self.cleaned_data['email']
            endpoint = 'https://disposable.debounce.io/?email={email_address}'
            url = endpoint.format(email_address=email)

            response = requests.get(url)
            checker = response.json()

            if checker['disposable'] == 'false':
                raise forms.ValidationError("Invalid Input")
            return checker
                
