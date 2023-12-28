from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, ContactSerializer, UserContactsSerializer

from rest_framework.views import APIView
from rest_framework import generics



#=============================================================================================
#                                 FUNCTION-BASED VIEWS                                       #
#=============================================================================================
# # Create your views here.
# @api_view(['GET', 'POST'])
# def users_view(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def single_user_view(request, pk):
    
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
    
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         serializer = UserSerializer(user, data=request.data, partial=request.method=='PATCH')
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



#=============================================================================================
#                                 CLASS-BASED VIEWS                                          #
#=============================================================================================
#Class based views
class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserContactsList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserContactsSerializer