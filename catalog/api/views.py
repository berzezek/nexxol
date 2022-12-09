from catalog.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, ProductPostSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


@api_view([ 'GET', 'POST' ])
@csrf_exempt
@permission_classes([ IsAuthenticatedOrReadOnly ])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view([ 'PUT', 'DELETE' ])
@csrf_exempt
@permission_classes([ IsAuthenticatedOrReadOnly ])
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        print(category)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view([ 'GET', 'POST' ])
@csrf_exempt
@permission_classes([ IsAuthenticatedOrReadOnly ])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.filter(category__isActive=True)
        paginator = LimitOffsetPagination()
        paginator.page_size = 100
        products_count = products.count()
        page_count = products.count()//paginator.page_size + 1
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return Response({'result': serializer.data,
                         'count': products_count,
                         'page_count': page_count})

    elif request.method == 'POST':
        serializer = ProductPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view([ 'GET', 'PUT', 'DELETE' ])
@csrf_exempt
@permission_classes([ IsAuthenticatedOrReadOnly ])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        category = Category.objects.get(id=request.data['category'])
        serializer = ProductPostSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view([ 'GET' ])
@csrf_exempt
@permission_classes([ IsAuthenticatedOrReadOnly ])
def product_post(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductPostSerializer(product)
        return Response(serializer.data)