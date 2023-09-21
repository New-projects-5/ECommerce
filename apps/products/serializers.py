from rest_framework import serializers

from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductsSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'category_name', 'name', 'slug', 'description', 'price', 'stock', 'is_available', 'created_time', 'updated_time']


class ProductCreateSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category.name')
    class Meta:
        model = Product
        fields = [ 'name', 'slug', 'description', 'price', 'stock', 'is_available']

    def validate(self, attrs):
        print(f"attrs in serializer: {attrs}")
        name = attrs.get("name", None)
        description = attrs.get("description", None)
        price = attrs.get("price", None)
        category_name = attrs.get('category_name', None)

        if name is None:
            raise serializers.ValidationError("name maydoni bo'sh bo'lishi mumkin emas")
        if description is None:
            raise serializers.ValidationError("description maydoni bo'sh bo'lishi mumkin emas")
        if price is None:
            raise serializers.ValidationError("price maydoni bo'sh bo'lishi mumkin emas")
        # if category_name is None:
        #     raise serializers.ValidationError("category_name maydoni bo'sh bo'lishi mumkin emas")
        return attrs

    # def create(self, validated_data):
    #     category_name = validated_data.get('category_name', None)
    #     category, created = Category.objects.get_or_create(name=category_name)
    #     validated_data['category'] = category
    #     new_product = Product.objects.create(**validated_data)
    #     # new_product.save()
    #     return new_product

    def create(self, validated_data):
        category_name = validated_data.pop("category_name")
        category, created = Category.objects.get_or_create(name=category_name)
        validated_data["category"] = category
        new_product = Product.objects.create(**validated_data)
        # new_product.save()
        return new_product