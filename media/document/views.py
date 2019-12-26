
from rest_framework.views import APIView
from rest_framework.response import Response
from decimal import Decimal
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product
from itertools import chain
class get_basket(APIView):

    def get(self, request, *args, **kwargs):
            exist=True
            list1=[{"goods_id":13, "number":5 ,"sum":13000} , {"goods_id":14, "number":3 , "sum":75000}]

            # exist=False
            # list1=[]
            return Response({"exist":exist ,"content":list1})


@api_view(['GET'])
def search(request,searched):
	products=Product.objects.filter(
				name__contains=searched).order_by('recordTime')[0:10]
	serializer=ProductSerializer(products,many=True)
	return Response(serializer.data)


@api_view(['GET'])
def searching(request,searched):
    searched_length=len(searched)
    products=Product.objects.filter(
                name__contains=searched).order_by('recordTime')
    
    for k in range(0,searched_length+1):
        products_length=len(products)


        if products_length > 2 :

            serializer=ProductSerializer(products[0:2],many=True)
            return Response(serializer.data)
            
        
        else : 
            new_products=Product.objects.filter(
                name__contains=searched[0:searched_length-k-1]).order_by('recordTime')
            products=list(chain(products,new_products))

   





