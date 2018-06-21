def converting_price(price, quantity=1):
    s = quantity*float((price.replace(',', "")[1:]))
    if len(str(s)) > 5:
        return ','.join(((price.replace(price[1:-1],str(s)))[:-6], (price.replace(price[1:-1],str(s)))[-6:]))
    else:
        return price.replace(price[1:-1], str(s))
