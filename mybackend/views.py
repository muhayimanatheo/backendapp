from django.shortcuts import render
from .models import *
from .serializers import*
from django .http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import APIView


# Create your views here.
def index(request):
    return render(request, "index.html")

@csrf_exempt
def UserRegisterApi(request):
    if request.method == 'GET':
        selectedData = UserRegister.objects.all()
        serializer = UserRegisterSerializer(selectedData, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def OperationByOne(request, id):
      try:
        checkid = UserRegister.objects.get(id=id)
      except UserRegister.DoesNotExist:
        return JsonResponse({'message': 'data not found'},status=404)
         
      if request.method == 'GET':     
        serializer = UserRegisterSerializer(checkid)
        return JsonResponse(serializer.data)
      elif request.method == 'DELETE':
          deletedata = UserRegister.objects.get(id=id).delete()
          return JsonResponse({'message': 'data deleted'})
      elif request.method == 'PUT':
          data = JSONParser().parse(request)
          serializer = UserRegisterSerializer(checkid, data=data)
          if serializer.is_valid():
              serializer.save()
              return JsonResponse(serializer.data)
          return JsonResponse(serializer.errors, status=400)
