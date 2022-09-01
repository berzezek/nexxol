from django.urls import path, include
from .views import (
  category_list, 
  category_delete,
  product_list, 
  product_detail,
  product_delete,
)

urlpatterns = [
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.authtoken')),

  path('category/', category_list),
  path('category/<int:id>/', category_list),
  path('category-delete/<int:category_id>/', category_delete),
  path('product/', product_list),
  path('product/<int:product_id>/', product_detail),
  path('product-delete/<int:product_id>/', product_delete),
]