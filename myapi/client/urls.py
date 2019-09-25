from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from client.views import UserViewSet,UserDetailViewSet,login,SendRequestViewSet,ReciveRequestViewSet,HistoryViewSet,UpdateHistoryByGiver,SeeNotification,GetCompany
from django.conf.urls import url
from rest_framework.authtoken.views import ObtainAuthToken


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'detailsusers', UserDetailViewSet)
router.register(r'sendrequest', SendRequestViewSet)
router.register(r'reciverequest', ReciveRequestViewSet)
router.register(r'history', HistoryViewSet)


urlpatterns = [
   
    url('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    url('auth/', ObtainAuthToken.as_view()),
    path('login/', login),
    path('historybygiver/', UpdateHistoryByGiver),
    path('seenotif/', SeeNotification),
    path('getcompany/', GetCompany),
 
    
]