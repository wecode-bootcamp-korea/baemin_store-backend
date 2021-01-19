from django.urls import path,include
from product     import views  

urlpatterns = [
    # path('/create',           ProductCreateView.as_view()), # 상품 생성
    path('/',                 ProductListView.as_view()),   # 메인 
    path('/<int:product_id>', ProductDetailView.as_view()), # 디테일 
    # path('/update/<int:product_id>',  ProductUpdateView.as_view()), # 상품 수정 
    # path('/delete/<int:product_id>',  ProductDeleteView.as_view()), # 상품 삭제
    
    # # 상품 좋아요
    # path('/<int:product_id>/like/create',  ProductCreateView.as_view()), 
    # path('/<int:product_id>/read/',        ProductListView.as_view()),  
    # path('/<int:product_id>/detail/',      ProductDetailView.as_view()), 
    # path('/update/<int:product_id>',       ProductUpdateView.as_view()), 
    # path('/delete/<int:product_id>',       ProductDeleteView.as_view()), 

    
]

