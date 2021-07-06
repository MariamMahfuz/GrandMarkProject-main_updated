from os import name
from django.conf.urls import url
from django.shortcuts import render, HttpResponseRedirect, render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from Grandhospital_App.models import appointment
from django.urls import reverse,reverse_lazy
from django.conf import settings
from Grandhospital_App.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from .forms import AppointmentForm

app_name='Grandhospital_App'

# Create your views here.

def index(request):
    dict={}
    return render(request, 'Grandhospital_App/index.html', context=dict)


# =============Send mail
#=============Send mail
class Contact(TemplateView):
    template_name = './Grandhospital_App/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message = "From: " + email + "/n"  " " + message

        mail = EmailMessage(subject, message, to = [settings.EMAIL_HOST_USER])
        mail.content_subtype = 'html'
        mail.send()
        return render(request, './Grandhospital_App/index.html')


def appoinment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AppointmentForm(request.POST)
            
            patient = request.user
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user_mail = request.POST.get('user_mail')
            gender = request.POST.get('gender')
            blood_group = request.POST.get('blood_group')
            phone = request.POST.get('phone')
            address = request.POST.get('address_1')
            problem = request.POST.get('problem')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zipcode = request.POST.get('zipcode')
            avatar = request.POST.get('avatar')
            
            appointment_ins = appointment(
                patient = patient,
                first_name = first_name,
                last_name = last_name,
                user_mail = user_mail,
                gender = gender,
                blood_group = blood_group,
                phone = phone,
                address_1 = address,
                problem = problem,
                city = city,
                state = state,
                zipcode = zipcode,
                avatar = avatar
            )

            appointment_ins.save()

            return HttpResponseRedirect("/")
        
        else:
            form = AppointmentForm(initial={
                'patient' : request.user.id,
                'first_name' : request.user.first_name,
                'last_name' : request.user.last_name,
                'user_mail' : request.user.email
                })

        dict={'form' : form}
        return render(request,'Grandhospital_App/Appointment.html', context=dict)
    else:
        return render(request, 'App_Login/sign_up.html')


def patient_list(request):
    appointment_db = appointment.objects.all()
    dict = {'patient_db' : appointment_db}
    return render(request, 'Grandhospital_App/patient_list.html', context=dict)

def cardiology(request):
    dict={}
    return render(request,'Grandhospital_App/Cardiology.html',context=dict)


def gynecology(request):
    dict={}
    return render(request,'Grandhospital_App/Gynecology.html',context=dict)

def medicine(request):
    dict={}

    return render(request,'Grandhospital_App/medicine.html',context=dict)

def surgery(request):
    dict={}

    return render(request,'Grandhospital_App/surgery.html',context=dict)

