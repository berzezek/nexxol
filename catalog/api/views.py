from catalog.models import Category, Product
from .serializers import CategorySerialier, ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


@api_view(['GET', 'POST', 'PUT'])
@csrf_exempt
@permission_classes([IsAuthenticatedOrReadOnly])
def category_list(request, id=None):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerialier(category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@csrf_exempt
# @permission_classes([IsAuthenticatedOrReadOnly])

def product_list(request, category_id=None, product_id=None):


    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method ==  'POST':
        try:
         category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @csrf_exempt
# @permission_classes([IsAuthenticatedOrReadOnly])
# def product_list(request, category_id=None):
#     products = Product.objects.all().filter(category__id=category_id)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)