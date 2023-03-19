from django import template


register=template.Library()

@register.filter(name='cart_quantity')
def cart_quantity(carts,cart):
    keys=cart.keys()
    for id in keys:
        if str(id)==carts.product.id:
            return cart.get(id)
    return 0;

    

