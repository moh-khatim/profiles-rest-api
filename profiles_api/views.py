from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloAPIView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_api_view = [
            '1',
            '2',
            '3',
        ]

        return Response({'message': 'hello', 'an_api_view': an_api_view})
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message":message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        return Response({'method': "PUT"})
    
    def patch(self, request, pk=None):
        return Response({'method': "PATCH"})
    
    def delete(self, request, pk=None):
        return Response({'method': "DELETE"})
    
class UserProfileViewSet(viewsets.ModelViewSet): 
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,)
    search_fields = ('name', 'email')

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES