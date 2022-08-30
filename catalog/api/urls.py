from django.urls import path, include
from .views import category_list, product_list, product_get

urlpatterns = [
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.authtoken')),

  path('category/', category_list),
  path('category/<int:id>/', category_list),
  path('product/', product_list),
  path('product/<int:product_id>/', product_get),
]