from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from product.views import category_list,sub_category_list, product_list

urlpatterns = [
    path('category_list/', category_list),
    path('sub_category_list/', sub_category_list),
    path('product_list/', product_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
