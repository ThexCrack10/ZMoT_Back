<<<<<<< HEAD
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
=======
from tablib import Dataset
from .resources import ProductResource
from django.shortcuts import render
#API
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import get_object_or_404

class ProductoList(generics.ListCreateAPIView):
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializer

        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

def simple_upload(request):
    if request.method == 'POST':
        product_resource = ProductResource()
        dataset = Dataset()
        new_products = request.FILES['myfile']

        imported_data = dataset.load(new_products.read())
        result = product_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            product_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

>>>>>>> d52a33efb512735425f940ba06297e9d2726dffb
