class ConvertingPrice:

    def convert_price_to_float(self,price, quantity=1):
        return quantity * float((price.replace(',', "")[1:]))

    def convert_float_to_price(self,float):
        price = "$1.00"
        second = None if len(str(float).split('.')[1]) > 1 else -1
        if len(str(float)) > 5:
            return ','.join(((price.replace(price[1:second],str(float)))[:-6], (price.replace(price[1:second],str(float)))[-6:]))
        else:
            return price.replace(price[1:second], str(float))


    def converting_price(self,price, quantity=1):
        s = self.convert_price_to_float(price, quantity)
        second = None if len(str(s).split('.')[1]) > 1 else -1
        if len(str(s)) > 5:
            return ','.join(((price.replace(price[1:second],str(s)))[:-6], (price.replace(price[1:second],str(s)))[-6:]))
        else:
            return price.replace(price[1:second], str(s))