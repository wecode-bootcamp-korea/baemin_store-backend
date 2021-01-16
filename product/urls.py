from django.urls import path,include
from product     import views  

urlpatterns = [
    path('/', views.ProductListView.as_view()),   
    # path('/<int:product_id>',   views.ProductDetailView.as_view()),
    
]

