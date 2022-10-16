from django.urls import path
from . import views


urlpatterns = [
    path( 'searchproducts' , views.searchproducts , name='searchproducts' ),
    path( '<int:pro_id>' , views.product , name='product' ),
    path('shop', views.products , name='shop'),
    path( 'search' , views.advancedsearch , name='search' ),
]