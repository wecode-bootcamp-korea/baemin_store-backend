from django.urls import path,include
from product     import views  

urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('/product_detail',views.ProductDetailView.as_view()),
] 
