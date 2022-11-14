from django import forms
from django.core.exceptions import ValidationError
from studentapp.models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

    def clean(self):
        """
        Raise `ValidationError` if user didn't provide both name and email.
        """
        cleaned_data = super().clean() # Making sure default cleaning is being done.
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        age = cleaned_data.get("age")
        
        if age < 18:
            raise forms.ValidationError('Must be at least 18 years old to register')

        if not name and not email:
            raise ValidationError("Please provide name or email.")
        
        return cleaned_data

