from django.urls import path, include
from .views import (
  category_list, 
  category_detail,
  product_list, 
  product_detail,
)

urlpatterns = [
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.authtoken')),

  path('category/', category_list),
  path('category/<int:id>/', category_detail),
  path('product/', product_list),
  path('product/<int:product_id>/', product_detail),
]