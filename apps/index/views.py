from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Index(APIView):
    def get(self, request):
        context = {
            'message': 'Ecommerce site successfully launched'
        }
        return Response(context, status=status.HTTP_200_OK)
