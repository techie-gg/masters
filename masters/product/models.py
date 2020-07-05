from django.db import models
from product.mixins import TimeMixin


class Category(TimeMixin):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(TimeMixin):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, models.DO_NOTHING,
                                 related_name='category', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"


class Product(TimeMixin):
    name = models.CharField(max_length=120)
    sub_category = models.ForeignKey(SubCategory, models.DO_NOTHING,
                                     related_name='sub_category')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'sub_category',)
        verbose_name = "Product"
        verbose_name_plural = "Products"

