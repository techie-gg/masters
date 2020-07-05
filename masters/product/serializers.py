from rest_framework import serializers

from product.models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category')


class ProductSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer()
    key = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'key', 'name', 'sub_category')

    def get_key(self, obj):
        return obj.id


class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'sub_category')
