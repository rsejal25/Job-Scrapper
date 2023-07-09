from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from login import models
from .scrappers import *
from .serializers import Subscribed_User_Serializer
from django.contrib.auth.models import User
from .models import Subscribed_Users
# Create your views here.
def home_page(request):
 return render(request,'home.html')

def search_page(request):
 return render(request,'search_page.html')

def profile_user_page(request):
 return render(request,'user_profile.html')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
 id=request.data['id']
 user=User.objects.filter(id=id)
 if user:
   username=user[0].username
 user_details=models.Login_USER.objects.filter(username=username)
 if user_details: 
   email=user_details[0].email
   l1=Subscribed_Users.objects.filter(email=email)
   serializer=Subscribed_User_Serializer(l1,many=True)
   if len(l1)>0:
     print(l1)
     return JsonResponse(serializer.data,safe=False)
   return JsonResponse({"success":True})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_user(request):
   print(request.body) 
   #email=request.data['email']
   id=request.data['id']
   #print(email)
   user=User.objects.filter(id=id)
   if user:
     username=(user[0].username);
     user=models.Login_USER.objects.filter(username=username)
     email=(user[0].email)
   designation=request.data['designation']
   location=request.data['location']
   print(email,designation,location)  
   webScrapper(designation,location)
   id=int(id)
   Subscribed_Users.objects.create(user_id=id,email=email,designation=designation,location=location)
   sendEmail(email)
   return JsonResponse({'success':True,'message':'user subscribed'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_designation_search(request):
  id=int(request.data['id'])
  print(id)
  user=Subscribed_Users.objects.filter(id=id)
  print(user)
  #user=user[0]
  user.delete();
  return JsonResponse({'success':'true'})