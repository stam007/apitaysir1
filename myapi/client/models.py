from django.db import models
from django.contrib.auth.models import User


from django.core.validators import MinLengthValidator
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import JSONField



class Details(models.Model):
    UserDetails = models.OneToOneField(User, related_name='details', on_delete=models.CASCADE)
    Picture = models.ImageField(blank=True, null=True)
    Phone = models.CharField('Phone Number', max_length=8, validators=[MinLengthValidator(8)], unique= True,blank=True, null=True)
    CIN = models.CharField('CIN Number', max_length=8, validators=[MinLengthValidator(8)], unique= True,blank=True, null=True)
    Address = models.TextField(null=True,blank=True)
    imageurl = models.TextField(blank=True,null=True,default=None)
    Type_Account =models.CharField(max_length=15,blank=True, null=True,default=None)
    Description = models.TextField(null=True,blank=True,default=None)


Request_Choices = (('Want Give Money', 'Want Give Money'),('Want Take Money', 'Want Take Money'),('Update Paiment', 'Update Paiment'))
class SendRequest(models.Model):
    
    id_User_Sender =models.ForeignKey(User, related_name='reciveuser',on_delete=models.CASCADE)
    id_User_Reciver = models.ForeignKey(User,related_name='senduser',on_delete=models.CASCADE)
    
    type_Request = models.CharField(max_length=20, choices=Request_Choices)
    
    Duration_Return_Money = models.IntegerField(blank=True,null=True)
    Amount = models.IntegerField()
    Aditionel_Information = models.TextField(blank=True,null=True)
    




class ReciveRequest(models.Model):
    
    ID_History = models.IntegerField(blank=True,null=True)
    id_User_Reciver = models.ForeignKey(User, related_name='reciveuserr',on_delete=models.CASCADE)
    id_User_Sender = models.ForeignKey(User, related_name='senduserr',on_delete=models.CASCADE)
    
    id_User_Giver = models.ForeignKey(User, related_name='usergiver',on_delete=models.CASCADE)
    id_User_Taken  = models.ForeignKey(User, related_name='usertaken',on_delete=models.CASCADE)
  
    Oroginal_Amount = models.IntegerField(blank=True,null=True)
    

    type_Request = models.CharField(max_length=20, choices=Request_Choices)

    Request_Information=models.TextField(blank=True,null=True)
    Date_Recive_Request = models.DateTimeField(blank=True,null=True,default=None)
    Is_Readed = models.BooleanField(default=False,blank=True,null=True)
    Is_See = models.BooleanField(default=False,blank=True,null=True)

    Accepted_Status_Giver = models.BooleanField(default=True,blank=True,null=True)
    Accepted_Status_Taken = models.BooleanField(default=True,blank=True,null=True)
    Decision_Status_User = models.BooleanField(default=True,blank=True,null=True)
   
  

class History(models.Model):
    
    
   
    
 
  
    data_User_Taken = models.ForeignKey(User, related_name='datausertaken',on_delete=models.CASCADE)
    data_User_Giver = models.ForeignKey(User, related_name='datausergiver',on_delete=models.CASCADE)
    
    Request_Information=models.TextField(blank=True,null=True)
    Date_Create_In_History = models.DateTimeField(blank=True,null=True)
    Oroginal_Amount = models.IntegerField()
    Paied_Amount = models.IntegerField()

    Paied_Now = models.IntegerField()

   
    Is_Paid = models.BooleanField(default=False,blank=True,null=True)
   
 

