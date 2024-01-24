from django.shortcuts import render
from .models import *
from .serializers import*
from django .http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


def UserRegisterApi(request):
    if request.method == 'GET':
        selectedData = UserRegister.objects.all()
        serializer = UserRegisterSerializer(selectedData, many=True)
    
        return JsonResponse(data=serializer.data, safe=False)