from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import APIAccess
import uuid

test_api_uuid = 'test_api_' + str(uuid.uuid4())
production_api_uuid = 'live_api_' + str(uuid.uuid4())
uuid_salt = uuid.uuid4()

@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many = True)
        return Response(user_serializer.data)
    
    if request.method == 'POST':
        data = request.data
        if data['email'] and data['password'] and data['first_name'] and data['last_name']:
            if len(User.objects.filter(username = data['email'])) >= 1:
                return Response({'message':'User already exist!'})
            if data['password'] == data['password_confirm']:
                user = User.objects.create_user(
                    username = data['email'],
                    password = data['password'],
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                )
                user.save()
                api_access = APIAccess(
                    user = user,
                    test_api = test_api_uuid,
                    production_api = production_api_uuid,
                    uuid = uuid_salt
                )
                api_access.save()
                user = User.objects.filter(pk = user.pk)
                user_serializer = UserSerializer(user, many = True)
                return Response(user_serializer.data)
            else:
                return Response({'message':'passwordes are not match'})
        return Response({'message':'all fields are required'})



def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        
    return render(request, 'create_customre/home.html')


def dashboard(request):
    if request.user.is_authenticated:
        api_access = APIAccess.objects.get(user = request.user)
        return render(request, 'create_customre/dashboard.html',{'api_access':api_access})
    return redirect('home')


def sign_up(request):
    message_success = False
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            if email and password and first_name and last_name:
                if len(User.objects.filter(username = email)) < 1:
                    user = User.objects.create_user(
                        username=email,
                        password=password,
                        first_name = first_name,
                        last_name = last_name
                    )
                    user.save()
                    api_access = APIAccess(
                        user = user,
                        test_api = test_api_uuid,
                        production_api = production_api_uuid,
                        uuid = uuid_salt
                    )
                    api_access.save()
                    message_success = True
        return render(request, 'create_customre/sign_up.html',{'message_success':message_success})
    return redirect('dashboard')


def log_out_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')




