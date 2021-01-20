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
# #     @login_required
# #     def get(self, request):
# #         try:
# #             data = json.loads(request.body)
# #             address = data['address']
# #             address = data['address']
# #             user = User.objects.filter(id=request.user.id)[0]

# #             if Address.objects.filter(user=user.id).filter(default=True).exists():
# #                 address = Address.objects.filter(user=user.id).filter(default=True)
# #             return address.get('address')

# #             Order.objects.create(
# #                 user    = request.user,
# #                 address = address,
# #                 point   = da
# #             )
#     pass