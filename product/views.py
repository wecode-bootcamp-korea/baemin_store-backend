import json
import re
from django.http             import JsonResponse
from django.views            import View


from product.models          import Product
from user.models             import User
from decorators.utils         import login_required


class ProductListView(View):  
    @login_required
    def get(self, request):
        try:
            products  = Product.objects.all()
            product_list = []
            for i in products:
                product_list.append(
                     {
                        'category'      :i.category.name,
                        'name'          :i.name,
                        'main_image'    :i.main_image,
                        'price'         :i.price,
                        'money_replace' :i.money_replace,
                        'create_at'     :i.create_at,
                        'update_at'     :i.update_at,
                        'tags'          :i.tags,
                        'hashtags'      :i.hashtags,
                        'sales'         :i.sales,
                    }
                )
            return JsonResponse({'RESULT':product_list }, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY ERROR OCCURED!'},status=400)

        except ValueError:
            return JsonResponse({'MESSAGE': 'VALUE ERROR OCCURED!'},status=400)

        except Product.DoesNotExist:
            return JsonResponse({'MESSAGE':'PRODUCT DOES NOT EXISTS!'},status=400)