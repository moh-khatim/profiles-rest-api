from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):

    def get(self, request, format=None):
        an_api_view = [
            '1',
            '2',
            '3',
        ]

        return Response({'message': 'hello', 'an_api_view': an_api_view})