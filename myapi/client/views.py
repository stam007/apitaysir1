from django.contrib.auth.models import User
from rest_framework import viewsets,mixins
from .models import Details,SendRequest,ReciveRequest,History
from client.serializers import UserSerializer,DetailsSerializer,SendRequestSerializer,ReciveRequestSerializer,HistorytSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework import filters
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
import json
from django.forms.models import model_to_dict
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.core import serializers
from django.db import connection
import datetime


from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)

    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['details']

  


 
    

    search_fields = ['first_name', 'last_name','email','username']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)


        user_details = Details.objects.create(UserDetails_id=serializer.data['id'])




        user = User.objects.get(id=serializer.data['id'])
        token = Token.objects.create(user=user)
        
        oi_dict = model_to_dict(token)
        oi_serialized = json.dumps(oi_dict)



        with connection.cursor() as cursor:
          
          result=cursor.execute('SELECT client_details.id as idd,client_details.Type_Account,client_details.Description,client_details.Picture,client_details.Phone,client_details.CIN,client_details.Address,client_details.imageurl,client_details.UserDetails_id,auth_user.* FROM client_details,auth_user WHERE  client_details.UserDetails_id ='+str(user.id)+' and auth_user.id='+str(user.id))
          
          item=[dict(zip([key[0] for key in cursor.description], row)) for row in result]
          
         
               
        return JsonResponse({'Data':item,'token': token.key})

   

        
  

class UserDetailViewSet(viewsets.ModelViewSet):
    
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer


    """filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['idc','name', 'idsc','prix']

    search_fields = ['name', 'idsc','prix']"""
  

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    
    with connection.cursor() as cursor:
          
          result=cursor.execute('SELECT client_details.id as idd,client_details.Type_Account,client_details.Description,client_details.Picture,client_details.Phone,client_details.CIN,client_details.Address,client_details.imageurl,client_details.UserDetails_id,auth_user.* FROM client_details,auth_user WHERE  client_details.UserDetails_id ='+str(user.id)+' and auth_user.id='+str(user.id))
          
          item=[dict(zip([key[0] for key in cursor.description], row)) for row in result]
          
          """if (item ==[]):
               result=cursor.execute('SELECT * FROM auth_user where auth_user.id='+str(user.id))
          
               item=[dict(zip([key[0] for key in cursor.description], row)) for row in result]"""
               
    return JsonResponse({'Data':item,'token': token.key})

   






class SendRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SendRequest.objects.all()
    serializer_class = SendRequestSerializer



   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        with connection.cursor() as cursor:
        
          id_User_Reciver = serializer.data['id_User_Reciver']
          Date_Recive_Request =  datetime.datetime.now()
  
          
          Is_Readed = False
          Is_See = False
          Accepted_Status_Giver = 'null'  
          Accepted_Status_Taken ='null'  
          phrase =' from you '
          phrase2=''
          id_User_Sender= serializer.data['id_User_Sender']
          
          
          type_Request =serializer.data['type_Request']
          if (type_Request =='Want Give Money'):
             
             Accepted_Status_Giver = True
             phrase =' to you '
             id_User_Giver = serializer.data['id_User_Sender']
             id_User_Taken = serializer.data['id_User_Reciver']
          else:
             Accepted_Status_Taken =True  
             id_User_Taken = serializer.data['id_User_Sender']
             id_User_Giver = serializer.data['id_User_Reciver']
             
             
          if (serializer.data['Aditionel_Information']!=''):
             
             phrase2=' with additional information : '+str(serializer.data['Aditionel_Information'])





          dataS=cursor.execute('SELECT * FROM client_details,auth_user WHERE  client_details.UserDetails_id ='+str(id_User_Sender)+' and auth_user.id='+str(id_User_Sender))
          
          Data_Sender=[dict(zip([key[0] for key in cursor.description], row)) for row in dataS]
          
          if (Data_Sender ==[]):
            dataS=cursor.execute('SELECT * FROM auth_user where auth_user.id='+str(id_User_Sender))
          
            Data_Sender=[dict(zip([key[0] for key in cursor.description], row)) for row in dataS]
          
          
          
          Request_Information = Data_Sender[0]['first_name']+' '+Data_Sender[0]['last_name'] +' send you request to '+request.data.get('type_Request')+phrase+ str(serializer.data['Amount'])+' TND For duration it will be about '+str(serializer.data['Duration_Return_Money'])+' month'+phrase2
          result=cursor.execute("INSERT INTO client_reciverequest (Oroginal_Amount,type_Request,id_User_Reciver_id,id_User_Sender_id,Request_Information,Date_Recive_Request,Is_Readed,Is_See,Accepted_Status_Giver,Accepted_Status_Taken,id_User_Taken_id,id_User_Giver_id,Decision_Status_User,ID_History) VALUES ("+str(serializer.data['Amount'])+",'"+str(type_Request)+"',"+str(id_User_Reciver)+","+str(id_User_Sender)+",'"+str(Request_Information)+"','"+str(Date_Recive_Request)+"',"+str(Is_Readed)+","+str(Is_See)+","+str(Accepted_Status_Giver)+","+str(Accepted_Status_Taken)+","+str(id_User_Taken)+","+str(id_User_Giver)+",False,0"")")
      
        return JsonResponse({'Data':'tt'})




def ManagerRequest(request):
    
    ID_History = request.data.get('ID_History')
    id_User_Taken = request.data.get('id_User_Taken')
    id_User_Reciver = request.data.get('id_User_Reciver')['id']
    id_User_Giver = request.data.get('id_User_Giver')
    type_Request =  request.data.get('type_Request')
    Oroginal_Amount =  request.data.get('Oroginal_Amount')


    Accepted_Status_Giver = request.data.get('Accepted_Status_Giver')
    Accepted_Status_Taken = request.data.get('Accepted_Status_Taken')

    





    Request_Information = request.data.get('Request_Information')

    if(id_User_Reciver==id_User_Giver):
       ID_Sender=id_User_Giver
       ID_Ceiver=id_User_Taken
       
    else:
       

       ID_Sender=id_User_Taken
       ID_Ceiver=id_User_Giver
    
    if((type_Request=='Update Paiment') &(Accepted_Status_Giver==True)):

       Paid_Status =False
       obj = History.objects.get(id=request.data.get('ID_History'))
       Current_Paid=model_to_dict(obj)['Paied_Amount']
       Global_Amount=model_to_dict(obj)['Oroginal_Amount']
       if(Current_Paid+request.data.get('Oroginal_Amount')==Global_Amount):
           Paid_Status=True

       History.objects.filter(id=request.data.get('ID_History')).update(Paied_Amount=Current_Paid+request.data.get('Oroginal_Amount'),Paied_Now=0,Is_Paid=Paid_Status)



       instance_request=ReciveRequest.objects.create(id_User_Sender_id=request.data.get('id_User_Giver'),id_User_Reciver_id=request.data.get('id_User_Taken'),
        id_User_Giver_id=request.data.get('id_User_Reciver')['id'],id_User_Taken_id=request.data.get('id_User_Taken'),Oroginal_Amount=request.data.get('Oroginal_Amount'),
        type_Request='Accepted Update',
        Date_Recive_Request=datetime.datetime.now(),
        Is_Readed=False,Is_See=False,Decision_Status_User=True)
    elif ( (type_Request=='Update Paiment') &(Accepted_Status_Giver==False)):
        
        instance_request=ReciveRequest.objects.create(id_User_Sender_id=request.data.get('id_User_Giver'),id_User_Reciver_id=request.data.get('id_User_Taken'),
        id_User_Giver_id=request.data.get('id_User_Giver'),id_User_Taken_id=request.data.get('id_User_Taken'),Oroginal_Amount=request.data.get('Oroginal_Amount'),
        type_Request='Refused Update',
        Date_Recive_Request=datetime.datetime.now(),
        Is_Readed=False,Is_See=False,Decision_Status_User=True)


    else:
        
      with connection.cursor() as cursor:
        if(Accepted_Status_Giver & Accepted_Status_Taken):
             data_User_Taken = id_User_Taken
             data_User_Giver = id_User_Giver
             Request_Information_History = Request_Information
             Date_Create_In_History =datetime.datetime.now()
             Paied_Amount =0
             Paied_Now =0
             Is_Paid =False
             type_Request='Accepted Request'
             cursor.execute("INSERT INTO client_reciverequest (Oroginal_Amount,type_Request,id_User_Reciver_id,id_User_Sender_id,Request_Information,Date_Recive_Request,Is_Readed,Is_See,Accepted_Status_Giver,Accepted_Status_Taken,id_User_Taken_id,id_User_Giver_id,Decision_Status_User,ID_History) VALUES ("+str(Oroginal_Amount)+",'"+str(type_Request)+"',"+str(ID_Ceiver)+","+str(ID_Sender)+",'"+str(Request_Information)+"','"+str(datetime.datetime.now())+"',False,False,"+str(Accepted_Status_Giver)+","+str(Accepted_Status_Taken)+","+str(id_User_Taken)+","+str(id_User_Giver)+",True,0"")")

             cursor.execute("INSERT INTO client_history (data_User_Taken_id,data_User_Giver_id,Date_Create_In_History,Request_Information,Paied_Amount,Oroginal_Amount,Paied_Now,Is_Paid) VALUES  ("+str(data_User_Taken)+","+str(data_User_Giver)+",'"+str(Date_Create_In_History)+"','"+str(Request_Information_History)+"',"+str(Paied_Amount)+","+str(Oroginal_Amount)+","+str(Paied_Now)+",False"")")

        elif (((not Accepted_Status_Giver) & (Accepted_Status_Taken))|((Accepted_Status_Giver) & ( not Accepted_Status_Taken))):
             type_Request='Refused Request'
             cursor.execute("INSERT INTO client_reciverequest (Oroginal_Amount,type_Request,id_User_Reciver_id,id_User_Sender_id,Request_Information,Date_Recive_Request,Is_Readed,Is_See,Accepted_Status_Giver,Accepted_Status_Taken,id_User_Taken_id,id_User_Giver_id,Decision_Status_User,ID_History) VALUES ("+str(Oroginal_Amount)+",'"+str(type_Request)+"',"+str(ID_Ceiver)+","+str(ID_Sender)+",'"+str(Request_Information)+"','"+str(datetime.datetime.now())+"',False,False,"+str(Accepted_Status_Giver)+","+str(Accepted_Status_Taken)+","+str(id_User_Taken)+","+str(id_User_Giver)+",True,0"")")



        else:
            
            cursor.execute("INSERT INTO client_reciverequest (Oroginal_Amount,type_Request,id_User_Reciver_id,id_User_Sender_id,Request_Information,Date_Recive_Request,Is_Readed,Is_See,Accepted_Status_Giver,Accepted_Status_Taken,id_User_Taken_id,id_User_Giver_id,Decision_Status_User,ID_History) VALUES ("+str(Oroginal_Amount)+",'"+str(type_Request)+"',"+str(ID_Ceiver)+","+str(ID_Sender)+",'"+str(Request_Information)+"','"+str(datetime.datetime.now())+"',False,False,"+str(Accepted_Status_Giver)+","+str(Accepted_Status_Taken)+","+str(id_User_Taken)+","+str(id_User_Giver)+",False,0"")")
          



    return JsonResponse({'Data':'ttt'})




def ManagerHistory(request,additiondata):
    
    
    instance_request=ReciveRequest.objects.create(ID_History=request.data.get('id'),id_User_Reciver_id=request.data.get('data_User_Giver')['id'],id_User_Sender_id=request.data.get('data_User_Taken')['id'],
    id_User_Giver_id=request.data.get('data_User_Giver')['id'],id_User_Taken_id=request.data.get('data_User_Taken')['id'],
    Oroginal_Amount=additiondata.data.get('Paied_Now'),type_Request='Update Paiment',
    Request_Information=request.data.get('data_User_Taken')['first_name']+' '+request.data.get('data_User_Taken')['last_name']+' Paid for you '+str(additiondata.data.get('Paied_Now'))+' ?',Date_Recive_Request=datetime.datetime.now(),
    Is_Readed=False,Is_See=False,
    Accepted_Status_Giver=None,Accepted_Status_Taken=True,
    Decision_Status_User=False)
          
          
          
         
    return JsonResponse({'Data':'rr'})    

class ReciveRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ReciveRequest.objects.all().order_by('id').reverse()
    serializer_class = ReciveRequestSerializer

    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_User_Reciver','Is_Readed','Is_See']

    

    
    def update(self, request, *args, **kwargs):

        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        ManagerRequest(serializer)
        return Response(serializer.data)


class HistoryViewSet(viewsets.ModelViewSet):
    
    queryset = History.objects.all().order_by('id').reverse()
    serializer_class = HistorytSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_User_Taken','data_User_Giver','Is_Paid']

    

    def update(self, request, *args, **kwargs):

        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        #self.perform_update(serializer)
        #print(request.data.get('Paied_Now'),serializer.data.get('data_User_Taken'))
        ManagerHistory(serializer,request)
        return Response(serializer.data)



@csrf_exempt
@api_view(["PUT"])
@permission_classes((AllowAny,))
def UpdateHistoryByGiver(request):
        Paid_Status=False
        if(request.data.get('Paied_Now')+request.data.get('Paied_Amount')==request.data.get('Paied_Amount')):
            Paid_Status=True
        History.objects.filter(id=request.data.get('id')).update(Paied_Amount=request.data.get('Paied_Now')+request.data.get('Paied_Amount'),Is_Paid=Paid_Status)

        
        return JsonResponse({'Data':'ttt'})


@csrf_exempt
@api_view(["PUT"])
@permission_classes((AllowAny,))
def SeeNotification(request):
        
        
        ReciveRequest.objects.filter(id=request.data.get('id')).update(Is_See=True)

        
        return JsonResponse({'Data':'OK'})    






@csrf_exempt
@api_view(["Get"])
@permission_classes((AllowAny,))
def GetCompany(request):
  


        
        
    with connection.cursor() as cursor:
          
          result=cursor.execute("SELECT * FROM client_details,auth_user WHERE  client_details.Type_Account=='company' AND  client_details.UserDetails_id = auth_user.id")
          
          item=[dict(zip([key[0] for key in cursor.description], row)) for row in result]
          #print(item[0])
          
          
       
          
          for v in item:
              if(v['Picture']):


                v['details']={'Picture':'http://127.0.0.1:8000/media/'+v['Picture'],'Phone':v['Phone'],'Address':v['Address'],'Description':v['Description'],'imageurl':v['imageurl'],'Type_Account':v['Type_Account']}

              else:
                v['details']={'Picture':v['Picture'],'Phone':v['Phone'],'Address':v['Address'],'Description':v['Description'],'imageurl':v['imageurl'],'Type_Account':v['Type_Account']}

           
        
    return JsonResponse({'Data':item})   