from django import forms 
from django.core import validators

#PASS THIS FUNCTION IN validators to validate a field
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Needs to start with Z")


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter Your email again")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(
        required = False, 
        widget = forms.HiddenInput,
        validators = [validators.MaxLengthValidator(0)]
        )

    name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    text.widget.attrs.update({'class': 'form-control'})

    #add custom validation
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher):
    #         raise forms.ValidationError('GOTCHA BOT!')
            
    #     return botcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make Sure that the emails match! ')