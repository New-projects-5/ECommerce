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

        extra_kwargs = {
            'id': {'read_only': True},
            'created_time': {'read_only': True},
            'updated_time': {'read_only': True}
        }


class ProductCreateSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['category', 'category_name', 'name', 'slug', 'description', 'price', 'stock', 'is_available']

    def validate(self, data):
        attrs = super().validate(data)

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
        if category_name is None:
            raise serializers.ValidationError("category_name maydoni bo'sh bo'lishi mumkin emas")

        return attrs

    def create(self, validated_data):
        category = Category.objects.filter(name=validated_data['category_name']).first()
        new_product = Product.objects.create(
            category=category,
            name=validated_data['name'],
            price=validated_data['price'],
            stock=validated_data['stock'],
            description=validated_data['description'],
            is_available=validated_data['is_available']
        )
        return new_product


# class ProductUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['category', 'name', 'description', 'price', 'stock', 'is_available']
#
#     def update(self, instance, validated_data):
#         instance.category = validated_data.get('category', instance.category)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.stock = validated_data.get('stock', instance.stock)
#         instance.is_available = validated_data.get('is_available', instance.is_available)
#         return instance


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock', 'is_available']
