import json 
import re
from django.http import JsonResponse
from django.views import View

from product.models import (Category,       Product, Stock,
                            ProductTag,     Tag,     Review
                            ProductHashTag, HashTag, ReviewImage,
                            ProductSale,    Sale,    DetalImage,
                            Like, 
                            )

class ProductListView(View):
    def get(self, request)
            query_strings = request.GET
            category      = query_string['category'] 
            page_number   = query_string['page_number'] 
            
            page          = int(request.GET.get('page', 1))
            max_page      = math.ceil(Product.objects.all().count()/20)
        
            if page > max_length:
                page = max_length
            if page <= 0:
                page = 1

            page_count = 20 * page
            offset     = limit - page_count
            limit      = page * page_count

            if not ('category' in query_strings or 'subcategory' in query_strings):
                products = Product.objects.all()[offset:limit]

            if 'category' in query_strings:
                category    = Category.objects.get(id=qu)

            categories   = Category.objects.all()
            ordering     = request.GET.get('ordering')
            categories     = request.GET.get('category')

            product_list = [{
                'category'      :product.category.id,
                'name'          :product.name,
                'main_image'    :product.main_image,
                'price'         :product.price,
                'mony_replace'  :product.mony_replace,
            } for product in products ]

            sort_type = {
                'date'      : 'nameupdate_at'
                'min_price' : 'price',
                'max_price' : '-price',
                'abc'       : 'name',
                'descabc'   : '-name' 
            }
            category_type = {
                'all'             :1,
                'stationary'      :2,
                'living'          :3,
                'book '           :4,
                'eulji-edition'   :5,
                'fun-edition'     :6,
                'baedal-friend'   :7,
                'preset-set'      :8,
                'collaboration'   :9,
            }

            if category in category_type:


            if category is not None:
                if ordering is not None:
                    products = Product.objects.filter(category_type[category]).order_by(sort_type[ordering]).prefetch_related('image_url')[offset:limit]
                else:
                    products = Product.objects.filter(category_type[category]).order_by('pub_date').prefetch_related('image_url')[offset:limit]
                if ordering == 'best':
                    products = Product.objects.filter(category_type[category]).annotate(Count('review')).order_by('-review__count').prefetch_related('image_url')[offset:limit]

            if ordering is not None and ordering != 'best':
                products = Product.objects.order_by(sort_type[ordering]).prefetch_related('image_url')[offset:limit]
            else:
                products = Product.objects.order_by('pub_date').prefetch_related('image_url')[offset:limit]
                
            if ordering == 'best':
                products = Product.objects.annotate(Count('review')).order_by('-review__count').prefetch_related('image_url')[offset:limit]
            
            for product in products:
                image = product.image_url
                product_dict = {
                    'category'       : product.category.category,
                    'name'           : product.name,
                    'price'          : product.price,
                    'description'    : product.description,
                    'thumnail_image' : image.first().image_url,
                    'sub_image'      : image.all()[1].image_url,
                    'pub_date'       : product.pub_date
                }
                product_list.append(product_dict)

            return JsonResponse({'product_list':product_list}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except Category.DoesNotExist:
            return JsonResponse({'MESSAGE':'CATEGORY_DOES_NOT_EXIST'}, status=404)
            
                            