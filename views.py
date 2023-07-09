from django.shortcuts import render
from .models import Login_USER
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.generic.list import ListView
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.generic import View
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class RegisterView(APIView):
 def post(self,request):
   username=request.data['username']
   password=request.data['password']
   address=request.data['address']
   email=request.data['email']
   h1=Login_USER.objects.create(username=username,email=email,address=address,password=password)
   print(username)
   print(password)
   user=User(username=username)
   user.set_password(password)
   user.save()
   user1=User.objects.get(username=username)
   print(user1.password)
   return Response({'status':'success'})
    

class LoginView(APIView):
  def post(self,request):
   email=request.data['email']
   password=request.data['password']
   #print(request.header)
   student=Login_USER.objects.get(email=email)
   if student.password!=password: return Response({'status':'fail'})
   if student:
     username=student.username
     print(username)
     user=User.objects.get(username=username)
     refresh=RefreshToken.for_user(user)
     return Response({'status':'success','refresh':str(refresh),'access':str(refresh.access_token)})
   else:
     return Response({'status':'fail'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show(request):
 users=Login_USER.objects.all()
 for i in users:
   print(i.username,i.address)
 serializer=LoginSerializer(users,many=True)
 return JsonResponse(serializer.data,safe=False)


def login_page(request):
 return render(request,'login.html')

def register_page(request):
 return render(request,'register.html')

def users_list(request):
 return render(request,'users.html')

def update_form(request):
 return render(request,'update_form.html')


def delete_form(request):
 return render(request,'delete_form.html')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
 id=int(request.GET['id'])
 user=Login_USER.objects.get(id=id)
 user.delete()
 return Response({'status':success})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
   id=int(request.data['id'])
   username=request.data['username']
   print('hello',username)
   password=request.data['password']
   address=request.data['address']
   email=request.data['email']
   user=Login_USER.objects.get(id=id)   
   user.username=username
   print(user.username,"**")
   user.password=password
   user.address=address
   user.email=email
   user.save()
   return Response({'status':'success'})

def users_details(request):
 id=int(request.GET['id'])
 user=Login_USER.objects.filter(id=id)
 serializer=LoginSerializer(user,many=True)
 print(user)
 return JsonResponse(serializer.data,safe=False)

def login1(request):
 if request.methods=='POST':
   email=request.POST['email']
   password=request.POST['password']
   print(email,password)
   student=Login_USER.objects.get(email=email)
   if student:
     user=User.objects.get(email=email)
     refresh=RefreshToken.for_user(user)
     return Response({'status':'success','refresh':str(refresh),'access':str(refresh.access_token)})