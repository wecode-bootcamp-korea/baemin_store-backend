from product.models import Product, Sale


def sale_options(items):
    if items.on_sales:
        status = items.on_sales.status
        rate   = items.on_sales.rate
    else:
        status = False
        rate   = None
    return {'status':status, 'rate':rate}