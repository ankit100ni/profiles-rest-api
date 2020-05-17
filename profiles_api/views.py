from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to django view',
            'Gives you most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello messaage with our name"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validate_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
