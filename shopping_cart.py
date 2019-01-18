class ShoppingCart:
    """ Class for defining a shopping cart. """
    
    def __init__(self, employee_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, new_total):
        self._total = new_total
        return self._total
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, list_of_items):
        self._items = list_of_items
        return self._items
    
    @property
    def employee_discount(self):
        return self._employee_discount
    
    @employee_discount.setter
    def employee_discount(self, new_emp_discount):
        self._employee_discount = new_emp_discount
        return self.employee_discount
    
    def get_attr(self, item, attr):
        return item[attr]
    
    def add_item(self, item, price, amount=1):
        self.total += price*amount
        for _ in range(amount):
            # Item name, price, and bool to indicate if discount is valid
            self.items.append(
                {
                 'Item': item,
                 'Price': price,
                })
        return self.total
    
    
    def mean_item_price(self):
        return round(sum(self.get_attr(item, 'Price') for item in self.items)/len(self.items), 2)
    
    
    def median_item_price(self):
        prices = sorted([self.get_attr(item, 'Price') for item in self._items])
        n = len(prices)
        if n == 1:
            return round(prices[0], 2)
        # Length is odd; get middle value
        if n % 2:
            return round(prices[n//2], 2)
        # Length is even; get mean of two middle values
        return round((prices[n//2-1] + prices[n//2])/2, 2)
    
    
    def apply_discount(self):
        if self.employee_discount:
            discount = self.employee_discount/100
            disc_total = self.total * (1 - discount)
            return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("
    
    
    def item_names(self):
        return [self.get_attr(item, 'Item') for item in self.items]
    
    
    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            "There are no items in your cart!"
        self.total -= removed_item['Price']
    
 