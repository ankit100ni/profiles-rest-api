from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to django view',
            'Gives you most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})
