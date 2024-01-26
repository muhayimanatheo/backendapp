from django.shortcuts import render
from .models import *
from .serializers import*
from django .http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

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

        
