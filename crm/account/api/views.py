from rest_framework.decorators import api_view
from account.models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render

@api_view(['GET'])
def customerView(request):
    customers = Customer.objects.all().order_by('id')
    serializer = CustomerSerializer(customers,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def customerCreateView(request):
    if request.method == 'GET':
        customers = Customer.objects.all().order_by('id')
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def game(request):
    return render(request,'fourdots.html',{})