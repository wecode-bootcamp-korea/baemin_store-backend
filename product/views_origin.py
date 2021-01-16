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

class ProductMainView(View):
    def get(self, request)
            PRODUCTS_IN_ONE_PAGE = 14
            query_strings = request.GET         
            page          = int(request.GET.get('page', 1))
            max_page      = math.ceil(Product.objects.all().count()/PRODUCTS_IN_ONE_PAGE)

            if page > max_page:
                page = max_page
            if page <= 0:
                page = 1

            limit     = PRODUCTS_IN_ONE_PAGE * page
            offset    = limit - PRODUCTS_IN_ONE_PAGE
            category = request.GET.get('category')
            ordering = request.GET.get('ordering')
            
            sorting = {
                'stock'     : '-stock'
                'date'      : 'update_at'
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

            products = Product.objects.\
                filter(orderlist__order__orderstatus_id=5).\
                select_related(
                    'seller',
                    'delivery',
                    'sale',
                    'category',
                    'sub_category'
                ).\
                prefetch_related(
                    'orderlist_set',
                    'review_set'
                ).\
                annotate(sum=Sum('orderlist__quantity')).\
                annotate(review_count=Subquery(
                    Review.objects.filter(product=OuterRef('pk')).values('product').
                        annotate(count=Count('pk')).values('count'))
                )



            if not ('category' in query_strings or 'ordering' in query_strings):
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
            
                            