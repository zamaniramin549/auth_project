from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.create_customre.models import *

@api_view(['GET', 'POST'])
def user_api(request):
    if request.method == 'GET':

        api_header = request.META.get('HTTP_API_KEY', None)
        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            customre = APIAccess.objects.get(production_api = api_header).user
        except:
            return Response({'message':'api header is incorrect!'})

        user_api = UserApi.objects.filter(customre = customre)
        user_api_serializer = UserApiSerializer(user_api, many = True)
        return Response(user_api_serializer.data)
    
    if request.method == 'POST':
        api_header = request.META.get('HTTP_API_KEY', None)
        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            customre = APIAccess.objects.get(production_api = api_header).user
        except:
            return Response({'message':'api header is incorrect!'})
        
        data = request.data
        if len(UserApi.objects.filter(user_email = data['email'], customre = customre)) >= 1:
            return Response({'message':'User already exist!'})
        if data['email'] and data['password']:
            user_api = UserApi(
                customre = customre,
                user_email = data['email'],
                user_password = data['password'],
                user_first_name = data['first_name'],
                user_last_name = data['last_name'],
            )
            user_api.save()
            user_api = UserApi.objects.filter(pk = user_api.pk)
            user_api_serializer = UserApiSerializer(user_api, many = True)
            return Response(user_api_serializer.data)
        else:
            return Response({'message':'Email and Password are required!'})
        

@api_view(['GET'])
def single_user_api(request, user_id):
    api_header = request.META.get('HTTP_API_KEY', None)
    if not api_header:
        return Response({'message':'api header is missing!'})
    
    try:
        customre = APIAccess.objects.get(production_api = api_header).user
    except:
        return Response({'message':'api header is incorrect!'})
    
    user_api = UserApi.objects.filter(customre = customre, id = user_id)
    user_api_serializer = UserApiSerializer(user_api, many = True)
    return Response(user_api_serializer.data)




@api_view(['GET', 'POST'])
def user_api_permission_name(request):
    if request.method == 'GET':

        api_header = request.META.get('HTTP_API_KEY', None)
        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            customre = APIAccess.objects.get(production_api = api_header).user
        except:
            return Response({'message':'api header is incorrect!'})


        user_api_permission_name = UserApiPermissionName.objects.filter(user = customre)
        user_api_permission_name_serializer = UserApiPermissionNameSerializer(user_api_permission_name, many = True)
        return Response(user_api_permission_name_serializer.data)
    
    

    if request.method == 'POST':
        api_header = request.META.get('HTTP_API_KEY', None)

        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            user = APIAccess.objects.get(production_api = api_header)
        except:
            return Response({'message':'api header is incorrect!'})
        
        data = request.data
        permission_name = data['permission_name'].lower()
        permission_name = permission_name.replace(' ', '_')
        
        if len(UserApiPermissionName.objects.filter(permission_name = permission_name, user = user.user)) >= 1:
            return Response({'message':'permission name is already exist'})
        
        user_api_permission_name = UserApiPermissionName(
            user = user.user,
            permission_name = permission_name
        )
        user_api_permission_name.save()
        user_api_permission_name = UserApiPermissionName.objects.filter(pk = user_api_permission_name.pk)
        user_api_permission_name_serializer = UserApiPermissionNameSerializer(user_api_permission_name, many = True)
        return Response(user_api_permission_name_serializer.data)
        


# @api_view(['GET', 'POST'])
@api_view(['POST'])
def user_api_permission(request):
    # if request.method == 'GET':


    #     api_header = request.META.get('HTTP_API_KEY', None)
    #     if not api_header:
    #         return Response({'message':'api header is missing!'})
        
    #     try:
    #         customre = APIAccess.objects.get(production_api = api_header).user
    #     except:
    #         return Response({'message':'api header is incorrect!'})

    #     user_api_permission = UserApiPermission.objects.all()
    #     user_api_permission_serialier = UserAPIPermissionSerializer(user_api_permission, many = True)
    #     return Response(user_api_permission_serialier.data)
    

    if request.method == 'POST':
        api_header = request.META.get('HTTP_API_KEY', None)

        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            user = APIAccess.objects.get(production_api = api_header)
        except:
            return Response({'message':'api header is incorrect!'})
        
        data = request.data

        permission_id = request.data['permission_id']
        user_id = request.data['user_id']


        if len(UserApi.objects.filter(customre = user.user)) >=1:
            if len(UserApiPermission.objects.filter(
                    user_api__id = user_id, 
                    user_api_permission_name__id = permission_id,
                    customre = user.user
                )) < 1:
                
                
                if data['read_permission']:
                    read_permission = True
                else:
                    read_permission = False



                if data['write_permission']:
                    write_permission = True
                else:
                    write_permission = False



                if data['edit_permission']:
                    edit_permission = True
                else:
                    edit_permission = False



                if data['delete_permission']:
                    delete_permission = True
                else:
                    delete_permission = False

                try:
                    user_api_permission_name = UserApiPermissionName.objects.get(pk = permission_id, user = user.user)
                except:
                    return Response({'message':'Permission does not exist'})
                
                try:
                    user_api = UserApi.objects.get(pk = user_id)
                except:
                    return Response({'message':'User not exist'})
                
                user_api_permission = UserApiPermission(
                    user_api_permission_name = user_api_permission_name,
                    user_api = user_api,
                    read = read_permission,
                    write = write_permission,
                    edit = edit_permission,
                    delete = delete_permission,
                    customre = user.user
                )
                user_api_permission.save()
                user_api_permission = UserApiPermission.objects.filter(pk = user_api_permission.pk)
                user_api_permission_serializer = UserAPIPermissionSerializer(user_api_permission, many = True)
                return Response(user_api_permission_serializer.data)
            else:
                return Response({'message':'User already have permission, Please edit the permission'})
        else:
            return Response({'message':'Something went wrong'})

        

@api_view(['DELETE'])
def delete_user_api(request):
    if request.method == 'DELETE':
        api_header = request.META.get('HTTP_API_KEY', None)
        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            user = APIAccess.objects.get(production_api = api_header)
        except:
            return Response({'message':'api header is incorrect!'})
        
        data = request.data['user_id']
        UserApi.objects.filter(pk = data, customre = user.user).delete()
        return Response({'message':'User deleted'})
    



@api_view(['DELETE'])
def delete_permission_name(request):
    if request.method == 'DELETE':
        api_header = request.META.get('HTTP_API_KEY', None)
        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            user = APIAccess.objects.get(production_api = api_header)
        except:
            return Response({'message':'api header is incorrect!'})
        
        data = request.data['permission_id']

        UserApiPermissionName.objects.filter(pk = data, user = user.user).delete()
        return Response({'message':'Permission deleted'})
    

@api_view(['DELETE'])
def delete_user_permission(request):
    if request.method == 'DELETE':
        api_header = request.META.get('HTTP_API_KEY', None)
        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            user = APIAccess.objects.get(production_api = api_header)
        except:
            return Response({'message':'api header is incorrect!'})
        
        data = request.data['user_permission_id']

        UserApiPermission.objects.filter(pk = data, customre = user.user).delete()
        return Response({'message':'User permission deleted'})
    


@api_view(['PUT'])
def edit_user_permission(request, user_permisson_id):
    if request.method == 'PUT':
        api_header = request.META.get('HTTP_API_KEY', None)
        if not api_header:
            return Response({'message':'api header is missing!'})
        
        try:
            user = APIAccess.objects.get(production_api = api_header)
        except:
            return Response({'message':'api header is incorrect!'})
        
        try:
            update_user_permission = UserApiPermission.objects.get(pk = user_permisson_id, customre = user.user)
        except:
            return Response({'message':'Permission is not exist!'})
        
        data = request.data

        if data['read_permission']:
            read_permission = True
        else:
            read_permission = False



        if data['write_permission']:
            write_permission = True
        else:
            write_permission = False



        if data['edit_permission']:
            edit_permission = True
        else:
            edit_permission = False



        if data['delete_permission']:
            delete_permission = True
        else:
            delete_permission = False

        update_user_permission.read = read_permission
        update_user_permission.write = write_permission
        update_user_permission.edit = edit_permission
        update_user_permission.delete = delete_permission
        update_user_permission.save()

        
        return Response({'message':'User permission updated'})

        


