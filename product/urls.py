from django.urls import path,include
from product     import views  

urlpatterns = [
    path('/product_list/<int:catergoryId>/<str:sorting>', views.ProductListView.as_view()),                           
]
