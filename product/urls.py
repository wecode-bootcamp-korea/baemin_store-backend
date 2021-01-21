from django.urls import path,include
from product     import views  

urlpatterns = [
    path('/product_list/<int:categoryId>/<str:sorting>', views.ProductListView.as_view()),
    path('/product_detail/<int:productId>',views.ProductDetailView.as_view()),
] 
