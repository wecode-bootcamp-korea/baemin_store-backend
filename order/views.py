# import json
# import re

# from django.http    import JsonResponse
# from django.views   import View

# from order.models   import (
#                             Order,
#                             OrderItem,
#                             OrderStatus,
#                             )
# from user.models    import User, Address
# from product.models import Product
# from decorators.utils     import login_required

# class OrderItemView(View):
#     @login_required
#     def get(self, request):
#         try:
#             data = json.loads(request.body)
#             address = data['address']
#             address = data['address']
#             user = User.objects.filter(id=request.user.id)[0]

#             if Address.objects.filter(user=user.id).filter(default=True).exists():
#                 address = Address.objects.filter(user=user.id).filter(default=True)
#             return address.get('address')

#             Order.objects.create(
#                 user    = request.user,
#                 address = address,
#                 point   = da
#             )
#     pass

#     @login_required
#     def post(self, request):
#         try:
#             data         = json.loads(request.body)
#             user         = Order.objects.filter(user=request.user) 
#             ORDER_STATUS = {
#                     1   :'입금대기',
#                     2   :'결제완료',
#                     3   :'상품준비중',
#                     4   :'배송중',
#                     5   :'배송완료',
#                     6   :'구매확정',
#             }

#             # I. Order 존재(O) 
#             #  1) 오더가 존재하고 이미 상품이 존재하는 카트 - 기존 OrderItem 업데이트(수량!)
#             #  2) 오더가 존재하고 상품이 새로 추가되는 경우 - OrderItem 생성(새로운 상품)          
            
#             # II.  Order 존재(X)
#             #  1) 오더를 생성 -> OrderItem 생성.
            
#             if Order.objects.filter(user=request.user).exists(): # Order(O) 
#                 if OrderItem.objects.filter(id=data['order_item_id']).exists(): # 이미 상품 존재
#                     order_item = OrderItem.objects.filter(id=data['order_item_id'])
#                     order_item.quantity += int(data['quantity']
#                     order_item.save()
#                 else: # 새로운 OrderItem 생성
#                     order_item = Order(
#                                         address     = data['address']
#                                         product_id  = data['product_id']
#                                         order       = 
#                                         total_price = 
#                                         thumbnail   = 
#                                         quantity    = 
#                     )
#                     order_item.save()



#             else:
#                 # Order.objects.create(
#                 #     user        = 
#                 # )

#             # except Order.DoesNotExist:
#             #     return None

#             if OrderItem.objects.filter(user=user):
#                 OrderItem.objects.create(
#                 user        = user,
#                 address     = user.address,
#                 product     = data['product_id'],
#                 quantity   += int(data['quantity']),
#                 thumbnail   = product.thumbnail,
#                 total_price = product.price,
#                 )
#             # return OrderItem.object.create(

#             # )

#             # return Cart(
#             #         quantity = data.get('quantity',)
#             #     )
            
        
#         except Product.DoesNotExist:
#             return JsonResponse({'MESSAGE': 'PRODUCT DOES NOT EXIST'}, status=400)
#         except User.DoesNotExist:
#             return JsonResponse({'MESSAGE': 'USER DOES NOT EXIST'}, status=400)
#         except KeyError:
#             return JsonResponse({'MESSAGE': 'KEY ERROR'}, status=400)
    