from rest_framework import generics
from rest_framework import permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from . import serializers
from .models import Product


class ProductListAPIView(APIView):
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

    def get(self, request):
        product = Product.objects.all().filter(is_available=True)
        serializer = serializers.ProductsSerializer(product, many=True)
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    def get(self, request, category, slug):
        product = get_object_or_404(Product, category__name=category, slug=slug)
        serializer = serializers.ProductsSerializer(product)
        return Response(
            {
                "success": True,
                "product": serializer.data
            }
        )



# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = serializers.ProductCreateSerializer
#     permission_classes = [permissions.IsAdminUser, ]


class ProductCreateAPIView(APIView):
    # permission_classes = [permissions.IsAdminUser, ]
    def post(self, request):
        serializer = serializers.ProductCreateSerializer(data=request.data)
        print(f"bu request in view: {request.data}")
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Mahsulot muvafaqiyatli qo'shildi",
                    "data": serializer.data
                }
            )
        else:
            return Response(
                {
                    "success": False,
                    "message": "Mahsulot qo'shishda xatolik",
                    "error": serializer.errors
                }
            )
