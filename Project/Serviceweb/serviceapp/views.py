from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from serviceapp.models import *

# Create your views here.

def index(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def contactus(request):
  template = loader.get_template('contactus.html')
  return HttpResponse(template.render({}, request))

def aboutus(request):
  template = loader.get_template('aboutus.html')
  return HttpResponse(template.render({}, request))

def aadhaar(request):
  template = loader.get_template('aadhaar.html')
  return HttpResponse(template.render({}, request)) 

def Add (request):
  template = loader.get_template('redirect.html')
  return HttpResponse(template.render({}, request))

def aadhaar_address_correction(request):
  template = loader.get_template('aadhaar-address-correction.html')
  return HttpResponse(template.render({}, request))

def Addrecord(request):
   if request.method =="POST":
    
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = Aadhaar_address_correction(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add')) 


def aadhaar_name_correction(request):
  template = loader.get_template('aadhaar-name-correction.html')  
  return HttpResponse(template.render({}, request))

def Addrecord1(request):
   if request.method =="POST":
    
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = Name_correction(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add'))





 

def aadhaar_dob_correction(request):
  template = loader.get_template('aadhaar-dob-correction.html') 
  return HttpResponse(template.render({}, request))


def Addrecord2(request):
   if request.method =="POST":
    
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = DOB_correction(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add'))

def pancard(request):
  template = loader.get_template('pan-card.html')
  return HttpResponse(template.render({}, request)) 

def new_pancard(request):
  template = loader.get_template('new-pan-card.html')
  return HttpResponse(template.render({}, request))

def Addrecord3(request):
   if request.method =="POST":
    
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = Pan_card_apply(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add'))

def re_pancard(request):
  template = loader.get_template('re-pan-card-correction.html')
  return HttpResponse(template.render({}, request))

def Addrecord4(request):
   if request.method =="POST":
    
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = re_pan_card_correction(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add'))

def re_print_pancard(request):
  template = loader.get_template('re-print-pan.html')
  return HttpResponse(template.render({}, request)) 

def Addrecord5(request):
   if request.method =="POST":
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = Pan_re_print(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add')) 

def passport(request):
  template = loader.get_template('passport.html')
  return HttpResponse(template.render({}, request)) 

def passport_major(request):
  template = loader.get_template('passport-major.html')
  return HttpResponse(template.render({}, request))

def Addrecord6(request):
   if request.method =="POST":
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = Passport_major(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add'))  

def passport_minor(request):
  template = loader.get_template('passport-minor.html')
  return HttpResponse(template.render({}, request)) 

def Addrecord7(request):
   if request.method =="POST":
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = Passport_minor(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add'))  

def voter_id(request):
  template = loader.get_template('voter-id.html')
  return HttpResponse(template.render({}, request)) 

def voter_id_new_apply(request):
  template = loader.get_template('voter-id-new-apply.html')
  return HttpResponse(template.render({}, request))

def Addrecord8(request):
   if request.method =="POST":
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = Voter_id_new_apply(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add')) 

def ration_card(request):
  template = loader.get_template('ration-card.html')
  return HttpResponse(template.render({}, request)) 

def new_ration_card(request):
  template = loader.get_template('new-ration-card.html')
  return HttpResponse(template.render({}, request))

def Addrecord9(request):
   if request.method =="POST":
    name =request.POST["name"]
    mobile =request.POST["mobile"]
    document =request.POST["document"]
    upload_document =request.POST["upload document"]
    your_message =request.POST["your message"]
    print(name,mobile,document,upload_document,your_message)
    ins = New_ration_card(name = name,mobile = mobile,document=document,upload_document=upload_document,your_message=your_message)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add'))  

  

