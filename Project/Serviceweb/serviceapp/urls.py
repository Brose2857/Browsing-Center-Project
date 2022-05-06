from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('contactus/',views.contactus, name = "contactus"),
    path('aboutus/',views.aboutus, name = "aboutus"),
    path('aadhaar/',views.aadhaar, name = "aadhaar"),
    path('Add/',views.Add, name = 'Add'),
    path('Aadhaar_address_correction/',views.aadhaar_address_correction, name = "aadhaar_address__correction"),
    path('Aadhaar_address_correction/Addrecord/',views.Addrecord, name = "Aadhaar_address_correction/Addrecord/"),
    
    path('Aadhaar_dob_correction/',views.aadhaar_dob_correction, name = "aadhaar_dob__correction"),
    path('Aadhaar_dob_correction/Addrecord2/',views.Addrecord2, name = "aadhaar_dob__correction/Addrecord2/"),
    
    path('Aadhaar_name_correction/',views.aadhaar_name_correction, name = "aadhaar_name__correction"),
    path('Aadhaar_name_correction/Addrecord1',views.Addrecord1, name = "aadhaar_name__correction/Addrecord1/"),
    
    
    path('pancard/',views.pancard, name = "pancard"),
    
    path('New_pancard/',views.new_pancard, name = "new_pancard"),
    path('New_pancard/Addrecord3/',views.Addrecord3, name = "new_pancard/Addrecord3"),
   
    path('Re_pancard/',views.re_pancard, name = "re_pancard"),
    path('Re_pancard/Addrecord4/',views.Addrecord4, name = "re_pancard/Addrecord4/"),
    
    path('Re_print_pancard/',views.re_print_pancard, name = "re_print_pancard"),
    path('Re_print_pancard/Addrecord5/',views.Addrecord5, name = "re_print_pancard/Addrecord5/"),
    

    path('passport/',views.passport, name = "passport"),


    path('passport_major/',views.passport_major, name = "passport_major"),
    path('passport_major/Addrecord6/',views.Addrecord6, name = "passport_major/Addrecord6/"),


    path('passport_minor/',views.passport_minor, name = "passport_minor"),
    path('passport_minor/Addrecord7/',views.Addrecord7, name = "passport_minor/Addrecord7/"),


    path('voter_id/',views.voter_id, name = "voter_id"),


    path('voter_id_new_apply/',views.voter_id_new_apply, name = "voter_id_new_apply"),
    path('voter_id_new_apply/Addrecord8/',views.Addrecord8, name = "voter_id_new_apply/Addrecord8/"),


    path('ration_card/',views.ration_card, name = "ration_card"),


    path('new_ration_card/',views.new_ration_card, name = "new_ration_card"),
    path('new_ration_card/Addrecord9/',views.Addrecord9, name = "new_ration_card/Addrecord9/"),
    
]