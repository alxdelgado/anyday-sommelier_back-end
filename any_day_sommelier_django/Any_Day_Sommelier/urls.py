from django.urls import path
from . import views

urlpatterns = [
  path('wines/', views.wine_list, name='wine_list'),
  path('wines/<int:pk>', views.wine_detail, name='wine_detail'),
  path('food/', views.food_list, name='food_list'),
  path('food/<int:pk>', views.food_detail, name='food_detail'),
  path('pairing/', views.pairing_list, name='pairing_list'),
  path('api/wines/', views.WineList.as_view(), name='wine-list'),
  path('api/wines/<int:pk>', views.WineDetail.as_view(), name='wine-detail'),
  path('api/food/', views.FoodList.as_view(), name='food-list'),
  path('api/food/<int:pk>', views.FoodDetail.as_view(), name='food-detail')
]
