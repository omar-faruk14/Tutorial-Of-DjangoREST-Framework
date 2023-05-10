from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def display(request):
    return render(request,'index.html')

class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello, World!", status=status.HTTP_200_OK)

from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET', 'POST'])
def homedata(request):
    context={
        "name": "Omar",
        "University": "North South University"
    }
    return Response(context)
