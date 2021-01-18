from django.urls import path,include
from product     import views  

urlpatterns = [
    path('/product_list/<int:catCd>/<str:sorting>', views.ProductListView.as_view()),                           

]