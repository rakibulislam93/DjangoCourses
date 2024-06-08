from django import forms
from profiles import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'