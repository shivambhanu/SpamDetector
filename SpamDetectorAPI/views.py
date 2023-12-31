from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AppUser, Contact
from .serializers import AppUserSerializer, ContactSerializer

from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated



# #=============================================================================================
# #                                 FUNCTION-BASED VIEWS                                       #
# #=============================================================================================
# # # Create your views here.
# # @api_view(['GET', 'POST'])
# # def users_view(request):
# #     if request.method == 'GET':
# #         users = User.objects.all()
# #         serializer = UserSerializer(users, many=True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = UserSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# # def single_user_view(request, pk):
    
# #     try:
# #         user = User.objects.get(pk=pk)
# #     except User.DoesNotExist:
# #         return Response(status=status.HTTP_404_NOT_FOUND)
    
    
# #     if request.method == 'GET':
# #         serializer = UserSerializer(user)
# #         return Response(serializer.data)
# #     elif request.method == 'PUT' or request.method == 'PATCH':
# #         serializer = UserSerializer(user, data=request.data, partial=request.method=='PATCH')
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #     elif request.method == 'DELETE':
# #         user.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)



# #=============================================================================================
# #                                 CLASS-BASED VIEWS                                          #
# #=============================================================================================
# #Class based views
# class UsersList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserContactsList(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserContactsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

# #Task: create an api endpoint to post contact to the user's who is posting it.
# class ContactsList(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
    
#     # def perform_create(self, serializer):
#     #     serializer.save(self.request.user)



    
class ListUsers(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    # permission_classes = [IsAuthenticated]


class RegisterUser(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    
    
# class AddContact(generics.CreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     permission_classes = [IsAuthenticated]
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)