from django.urls import path, include
from .views import category_list, product_list

urlpatterns = [
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.authtoken')),

  path('category/', category_list),
  path('category/<int:id>/', category_list),
  path('category/products/', product_list),
  path('category/<int:category_id>/product/', product_list),
]