from django import forms
from django.db.models import fields
from .models import appointment


class ContactForm(forms.Form):
    email = forms.EmailField()

# Appointment model form

class form_DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"
    def __init__(self, **kwargs):
        kwargs["format"] = "%d/%m/%y %H:%M:%S"
        super().__init__(**kwargs)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = [
            'patient',
            'first_name',
            'last_name',
            'user_mail',
            'dob',
            'gender',
            'blood_group',
            'phone',
            'address_1',
            'problem',
            'city',
            'state',
            'zipcode',
            'avatar'
        ]

        exclude = ('dob',)

        widgets = {
            'dob' : form_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"], attrs={
                'class' : 'form-control'
            }),

            'patient' : forms.TextInput(attrs={
                'class' : 'patient',
                'type' : 'hidden'
            }),

            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Your First Name'
            }),
            
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Your Last Name'
            }),

            'user_mail' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Your Email'
            }),

            'gender' : forms.Select(attrs={
                'class' : 'form-control'
            }),

            'blood_group' : forms.Select(attrs={
                'class' : 'form-control'
            }),

            'phone' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter your Phone Number here'
            }),

            'address_1' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Your Permanent Address Here',
                'id' : 'inputAddress'
            }),

            'problem' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Brief Your Problem In One Line',
                'id' : 'inputAddress2'
            }),

            'city' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'inputCity',
                'placeholder' : 'The City You Are In Now'
            }),

            'state' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'inputState',
                'placeholder' : 'State'
            }),

            'zipcode' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'id' : 'inputZip'
            }),

            'avatar' : forms.FileInput(attrs={
                'class' : 'form-control'
            })
        }