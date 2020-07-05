from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product, Category, SubCategory
from product.serializers import CategorySerializer, SubCategorySerializer, \
    ProductSerializer, ProductAddSerializer


@api_view(['GET'])
def category_list(request):
    """
    List all categories.
    """
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def sub_category_list(request):
    """
    List all sub categories.
    """
    if request.method == 'GET':
        category_id = request.GET.get("category_id")
        sub_categories = SubCategory.objects.select_related('category').all()
        if category_id:
            sub_categories = sub_categories.filter(category_id=category_id)
        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all product and add new product.
    """
    if request.method == 'GET':
        products = Product.objects.select_related('sub_category',
                                                  'sub_category__category')\
            .all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ProductAddSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            new_data = ProductSerializer(serializer.instance)
            return Response(new_data.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
