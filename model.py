def converting_price(price, quantity=1):
    s = quantity*float((price.replace(',', "")[1:]))
    return ','.join(((price.replace(price[1:-1],str(s)))[:-6], (price.replace(price[1:-1],str(s)))[-6:]))