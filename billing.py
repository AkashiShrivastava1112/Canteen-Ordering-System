def calculate_bill(cart,menu):
    total=0
    for order in cart:
        if order in menu:
            price=menu[order]
            total=total+price
    return total
def apply_discount(total, discount_percent):
    discount=total-(total*discount_percent/100)
    return discount
