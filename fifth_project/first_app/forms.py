from django import forms
from django.core import validators

class contactForm(forms.Form):

    name = forms.CharField(label='Full Name : ',initial="Rakib",help_text="Total length must be 50 characters",required=False,disabled=True)
    # file = forms.FileField()
    email = forms.EmailField(
    label="Useremail: ",
    widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    Age = forms.CharField(widget=forms.NumberInput)
    # Weight = forms.FloatField()
    # balance = forms.DecimalField()
    # Check = forms.BooleanField()
    Birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' }))
    Appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    Size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    
    MEAL = [('B','Bergar'),('S','Suf'),('M','Mashroom')]
    pizza = forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)



# class studentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']

#     #     if len(valname)<10:
#     #         raise forms.ValidationError('Enter a name with at least 10 characters')

#     #     else:
#     #         return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if ".com" not in valemail:
#     #         raise forms.ValidationError('Your email must contain .com')
            
#     #     else:
#     #         return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']

#         if len(valname) < 10:
#             raise forms.ValidationError('Enter a name with at least 10 characters')
        
#         if '.com' not in valemail:
#             raise forms.ValidationError('Your email must contain .com')

class studentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your name'}),validators=[validators.MaxLengthValidator(10,message='Enter name maximum 10 characters'),validators.MinLengthValidator(5,'Enter a name with at lease 5 characters')])

    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Type your email'}),validators=[validators.EmailValidator(message='Enter a valid email')])

    age = forms.IntegerField(validators=[validators.MaxValueValidator(35,message='age must be less 35'),validators.MinValueValidator(18,message='age must be 18')])

    file = forms.FileField(
        validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message = '.pdf .png Only')])
    

class passwordProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirmPassword']

        if val_pass != val_conpass:
            raise forms.ValidationError("password doesn't mathch")