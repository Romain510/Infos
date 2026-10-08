class Product:
    code=""
    name=""
    priceET=200.0
    
    def get_price_it(self,tax):
        price=(self.priceET+self.priceET*tax)
        return price

print(Product().get_price_it(0.5))