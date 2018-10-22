#from django.shortcuts import render
#import json
#from django.views.decorators.csrf import csrf_exempt
#from django.http import JsonResponse
#from backend.models import Producto 

# Create your views here.
#@csrf_exempt
#def insertarProducto (request):
#    json_data =json.loads(request.body)
#    producto = Producto(**json_data)
#    producto.save()
#    return JsonResponse(("msg":"se guardo"))