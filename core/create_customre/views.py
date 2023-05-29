from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import APIAccess
import uuid

test_api_uuid = 'test_api_' + str(uuid.uuid4())
production_api_uuid = 'live_api_' + str(uuid.uuid4())

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
                    last_name = data['last_name']
                )
                user.save()
                api_access = APIAccess(
                    user = user,
                    test_api = test_api_uuid,
                    production_api = production_api_uuid,
                )
                api_access.save()
                user = User.objects.filter(pk = user.pk)
                user_serializer = UserSerializer(user, many = True)
                return Response(user_serializer.data)
            else:
                return Response({'message':'passwordes are not match'})
        return Response({'message':'all fields are required'})





