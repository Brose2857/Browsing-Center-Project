from django.db import models

# Create your models here.



class Aadhaar_address_correction(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.FileField(upload_to ='files/',null=True,verbose_name = '')
  your_message = models.CharField(max_length=255)
  
class DOB_correction(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255)
  
class Name_correction(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255)
  
class Pan_card_apply(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255)
  
class re_pan_card_correction(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255) 
  
class Pan_re_print(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255)

class Passport_major(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255)
  
class Passport_minor(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255)
  
class New_ration_card(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255)
  
class Voter_id_new_apply(models.Model):
  name = models.CharField(max_length=30)
  mobile = models.CharField(max_length=100)
  document = models.CharField(max_length=100)
  upload_document = models.CharField(max_length=255)
  your_message = models.CharField(max_length=255)
