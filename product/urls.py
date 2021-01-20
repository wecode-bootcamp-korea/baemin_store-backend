from django.urls import path,include
from product     import views  

urlpatterns = [
    path('/product_list/<int:catergoryId>/<str:sorting>', views.ProductListView.as_view()),                           
    path('/',                 ProductListView.as_view()),   # 메인 
    path('/<int:product_id>', ProductDetailView.as_view()), # 디테일 
] 
