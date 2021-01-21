import json
import re
from django.http             import JsonResponse
from django.views            import View


from product.models          import Product, Sale
from user.models             import User
from decorators.utils        import login_required
from product.utils           import sale_options

import operator

class ProductListView(View):  
    def get(self,request, categoryId, sorting):
        try:
            items_per_page = 16
            sort_type = {
                'all'      :'id',
                'low_price':'price',
                'high_price':'-price',
                'new':'create_at'
                }
            if categoryId ==0:
                products = Product.objects.select_related("on_sales").order_by(sort_type[sorting])
            else:
                products = Product.objects.select_related("on_sales").filter(category_id=categoryId).order_by(sort_type[sorting])
            
            products_count  = products.count()
            product_list = []
            page_list = []
            
            for items in products:
                sales_option=sale_options(items)               
                item = {
                            'product_id'    :items.id,
                            'name'          :items.name,
                            'main_image'    :items.main_image,
                            'price'         :items.price,
                            'money_replace' :items.money_replace,
                            'create_at'     :items.create_at,
                            'on_sale'       :sales_option['status'],
                            'rate'          :sales_option['rate'],
                            'stock_status'  :items.stock_set.all()[0].quantity,
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


class ProductDetailView(View):
    def get(self,request,productId):
        try:
            product=Product.objects.select_related("on_sales").get(id=productId)
            sales_option=sale_options(product)
            detail_urls=[]
            item = {
                        'name'          :product.name,
                        'main_image'    :product.main_image,
                        'price'         :product.price,
                        'money_replace' :product.money_replace,
                        'on_sale'       :sales_option['status'],
                        'rate'          :sales_option['rate'],
                        'stock_status'  :product.stock_set.all()[0].quantity,
                        'product_images':[urls.detail_url for urls in product.productimage_set.all().order_by('image_flow')]
                    }
            return JsonResponse({'RESULT':item}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY ERROR OCCURED!'},status=400)

        except ValueError:
            return JsonResponse({'MESSAGE': 'VALUE ERROR OCCURED!'},status=400)

        except Product.DoesNotExist:
            return JsonResponse({'MESSAGE':'PRODUCT DOES NOT EXISTS!'},status=404)
