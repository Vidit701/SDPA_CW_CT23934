class Supplier:
    '''
    -This class represents a supplier for a coffee shop.
    -Attributes: 
        name: The supplier's name.
        prices A dictionary that contains the prices of various ingredients.
    -The supplier that is automatically selected is called 'Hasty' and it has pre-set prices for items such as Milk, Beans, and Spices.
    '''
    def __init__(self, name='Hasty', prices={'Milk': 0.3, 'Beans': 0.10, 'Spices': 0.05}):
        '''
        -Initializes the Supplier instance
        -prices (dict): A dictionary that contains the prices of various ingredients. Defaults to {'Milk': 0.3, 'Beans': 0.10, 'Spices': 0.05}.
        '''
        self.name = name
        self.prices = prices

    def purchase_ingredients(self, shop, quantities):
        '''
        -Assists in acquiring the necessary ingredients for the coffee shop.
        -The function goes through the requested ingredients and their quantities, calculates the cost, and updates the shop's pantry and cash balance accordingly.
        -If there is not enough money to buy an ingredient, it will display a message indicating the lack of funds.
        -Specifications:
            shop (CoffeeShop): The coffee shop making the purchase.
            quantities (dict): A dictionary that maps ingredients to the quantities that need to be purchased.
        -Special cases:
            An error occurred: ValueError. It will be caught and printed.
        """

        '''
        try:
            for ingredient, quantity_needed in quantities.items():
                cost = quantity_needed * self.prices[ingredient]
                if shop.cash_balance >= cost:
                    shop.pantry[ingredient] += quantity_needed
                    shop.cash_balance -= cost
                    print(f"Restocked {quantity_needed:.2f} {ingredient} for £{cost:.2f}")
                else:
                    print(f"Can't restock {ingredient}, insufficient funds, need {cost:.2f} but only have {shop.cash_balance:.2f}")
        except ValueError as e:
            print(f"Error purchasing ingredients: {e}")
           
               
# Jupyter Notebook Cell 2

# Define coffee-related constants
coffee_demand = {'Espresso': 500, 'Americano': 200, 'Filter': 300, 'Macchiato': 400, 'Flat White': 600, 'Latte': 1000}
coffee_prices = {'Espresso': 1.5, 'Americano': 2.5, 'Filter': 1.5, 'Macchiato': 3.0, 'Flat White': 3.5, 'Latte': 4.0}
coffee_ingredients = {'Espresso': {'Milk': 0.0, 'Beans': 8, 'Spices': 0}, 'Americano': {'Milk': 0.0, 'Beans': 6, 'Spices': 0},
                      'Filter': {'Milk': 0.0, 'Beans': 4, 'Spices': 0}, 'Macchiato': {'Milk': 0.1,'Beans': 8, 'Spices': 2},
                      'Flat White': {'Milk': 0.2, 'Beans': 8, 'Spices': 1}, 'Latte': {'Milk': 0.3, 'Beans': 8, 'Spices': 3}}
coffee_preparation_time = {'Espresso': 0.05, 'Americano': 0.0333, 'Filter': 0.0167, 'Macchiato': 0.0667,
                           'Flat White': 0.0833,
                           'Latte': 0.1}

# Define pantry capacities
pantry_capacity = {'Milk': 300, 'Beans': 20000, 'Spices': 4000}