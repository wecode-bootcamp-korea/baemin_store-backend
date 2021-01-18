import json
import re
from django.http             import JsonResponse
from django.views            import View


from product.models          import Product, Sale
from user.models             import User
from decorators.utils        import login_required

import operator

class ProductListView(View):  
    # @login_required
    def get(self,request, catCd, sorting):
        try:
            items_per_page = 16
            sort_type = {
                'low_price':'price',
                'high_price':'-price',
                'new':'create_at'
                }
            if catCd ==0:
                products = Product.objects.all().order_by(sort_type[sorting])
            else:
                products = Product.objects.filter(category_id=catCd).order_by(sort_type[sorting])
            
            products_count  = products.count()
            product_list = []
            page_list = []
            products.order_by('price')
            
            # for i in products:
            #     # if Sale.objects.filter(products_id=products.id).exists():
            #         sales_status = True
            #         product_list.append(
            #             {
            #                 'name'          :i.name,
            #                 'main_image'    :i.main_image,
            #                 'price'         :i.price,
            #                 'money_replace' :i.money_replace,
            #                 # 'sales_status'  :i.
            #             }
            #         )
            for items in products:   
                item = {
                            'name'          :items.name,
                            'main_image'    :items.main_image,
                            'price'         :items.price,
                            'money_replace' :items.money_replace,
                            'create_at'     :items.create_at,
                        }
                page_list.append(item)

                if len(page_list) == items_per_page:
                    product_list.append(page_list)
                    page_list = []
                    

                               
            return JsonResponse({'RESULT':product_list,'product_count':products_count}, status=200, safe=True)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY ERROR OCCURED!'},status=400)

        except ValueError:
            return JsonResponse({'MESSAGE': 'VALUE ERROR OCCURED!'},status=400)

        except Product.DoesNotExist:
            return JsonResponse({'MESSAGE':'PRODUCT DOES NOT EXISTS!'},status=404)
