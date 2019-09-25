from django.contrib.auth.models import User
from client.models import Details,SendRequest,ReciveRequest,History
from rest_framework import serializers

from rest_framework.response import Response
from django.http import JsonResponse
class DetailsSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Details
        fields =  '__all__'




class UserSerializer(serializers.ModelSerializer):
    details = DetailsSerializer(many=False, read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','last_name','details')
        extra_kwargs ={'password':{'write_only': True , 'required':True}}

    def create(self, validated_data):
          
           user=User.objects.create_user(**validated_data)
           
           return user

class SendRequestSerializer(serializers.ModelSerializer):
    #id_User_Sender = UserSerializer(many=False, read_only=True)

    class Meta:
        model = SendRequest
        fields =  '__all__'


class ReciveRequestSerializer(serializers.ModelSerializer):
   
    id_User_Reciver = UserSerializer(many=False, read_only=True)
    id_User_Sender = UserSerializer(many=False, read_only=True)
    #id_User_Giver = UserSerializer(many=False, read_only=True)
    #id_User_Taken = UserSerializer(many=False, read_only=True)
    class Meta:
        model = ReciveRequest
        fields = '__all__'
class HistorytSerializer(serializers.ModelSerializer):
   
    data_User_Taken = UserSerializer(many=False, read_only=True)
    data_User_Giver = UserSerializer(many=False, read_only=True)
    class Meta:
        model = History
        fields = '__all__'