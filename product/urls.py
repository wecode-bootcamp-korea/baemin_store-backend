from django.urls import path,include
from product     import views  

urlpatterns = [
    path('/all', views.ProductListView.as_view()),                           

]