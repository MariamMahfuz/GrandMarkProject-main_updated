from django.conf.urls import url
from django.urls import path
from Grandhospital_App import views

app_name='Grandhospital_App'

urlpatterns=[
    path('index/',views.index,name='index'),
    path('',views.index,name='index'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('patientList', views.patient_list, name='patientList'),
    path('appointment/',views.appoinment,name='appoinment'),
    path('cardiology/',views.cardiology,name='cardiology'),
    path('gynecology/',views.gynecology,name='gynecology'),
    path('medicine/',views.medicine,name='medicine'),
    path('surgery/',views.surgery,name='surgery'),
]