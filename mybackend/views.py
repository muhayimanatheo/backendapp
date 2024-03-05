from django.shortcuts import render
from .models import *
from .serializers import *
from django .http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.views import APIView


# Create your views here.
def index(request):
    return render(request, "index.html")
    
    # class BlogsApi(APIView):
    #     def post(self, request, *args, **kwargs):
    #         serializers = BlogsSerializer(data=request.data)
    #         if serializers.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response( serializer.data, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['GET', 'POST'])
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
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error("serializer error: %s", serializer.error)
        return JsonResponse(serializer.errors, status=400)
#blogs api requisted from backend
@csrf_exempt
@api_view(['GET', 'POST'])
def BlogApi(request):
       if request.method == 'GET':
            selectedData = Blogs.objects.all()
            serializer = BlogsSerializer(selectedData, many=True)
            return JsonResponse(data = serializer.data, safe=False)
        
       elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = BlogsSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error("serializer error: %s", serializer.error)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@csrf_exempt
@api_view(['GET', 'delete', 'PUT'])
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
      
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})
