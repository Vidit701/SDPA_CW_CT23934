import math
from Barista import Barista
from Supplier import Supplier


class CoffeeShop:
   
    """
    CoffeeShop Python class initializer puts up coffee shop simulation properties
   
    """
   
    def __init__(self, name='Boost', cash_balance=10000, max_baristas=4):
        """
        Initializes the coffee shop's properties including name, cash balance, and maximum baristas
        which are been set using the default values I am setting the coffeeshop name to Boost as given in the spec.

        """
        self.name = name #Initialising the name of the coffeeshop to Boost as it was stated in the spec
        self.cash_balance = cash_balance # cash_balance at the beginning of the first month is set to 10000
        self.max_baristas = max_baristas
        self.baristas = [] #creating an empty list for baristas and appending in next functions as we add the baristas
        self.pantry = {'Milk': 300, 'Beans': 20000, 'Spices': 4000}
        self.ingredient_depreciation = {'Milk': 0.4, 'Beans': 0.1, 'Spices': 0.1}
        self.pantry_costs = {'Milk': 0.1, 'Beans': 0.001, 'Spices': 0.001}
        self.rent_utilities_cost = 1500 #fixed rent of 1500£ to be deducted every month
        self.pantry_depreciation = {'Milk': 0, 'Beans': 0, 'Spices': 0} #initialising pantry_depreciation to 0 



    def add_barista(self, name, hourly_rate, specialty=None):
        """
        The aim of this function is to add new baristas to the shop simulation and
        is called the main.py while running the simulation.

        Parameters:
        - name (str): Name of the barista.
        - hourly_rate (float): The hourly rate of the barista.
        - specialty (str, optional): The specialty of the barista. Defaults to None.

        Raises:
        ValueError: If there is an error adding the barista (invalid input).

        Notes:
        - I check that whenever barista with the same name already exists;
          it prompts the user to enter another name.
        - Ensures that the total number of baristas does not exceed the maximum limit which is 4.
        - If both the conditions are met, it adds the barista to the simulation.

        """
        try:
            already_exists_baristas = [barista.name.lower() for barista in self.baristas]
            if name.lower() in already_exists_baristas: 
                # while comparing the existing names and the new inputs I am making sure that its converted to lower case 
                #to avoid case sensitivity issues. 
                print(f"A barista with the name '{name}' already exists. Please enter a different name.")
                name = input("Enter a new barista name: ")
                return

            if len(self.baristas) >= self.max_baristas:
                print(f"Cannot add {name}. Maximum baristas reached.")
                return

            barista = Barista(name, hourly_rate, specialty)
            self.baristas.append(barista)
            print(f"Added Barista {name}, at an hourly rate={hourly_rate}")

        except ValueError as e:
            print(f"Error adding barista: {e}")


   
    def remove_barista(self, barista):
        """
        This function is used to remove a barista from the coffee shop.

        Here I first check whether the barista to be removed already exists or not.
        If it exists then I delete it from the list of baristas and 
        again here I make sure it handles case sensitive issues while I use it in main.py. 
        In the event that this is not the case, a message is printed indicating that the barista that was
        specified does not exist in the list of baristas.
       
        Additionally, it checks if there will be at least one barista left after the removal.

        """
        if barista in self.baristas:
            if len(self.baristas) > 1:
                self.baristas.remove(barista)
                print(f"Removing the barista from the shop {barista.name}")
            else:
                print(f"Cannot remove {barista.name}. It is necessary to have at least one barista.")
        else:
            print(f"{barista.name} does not exist in the baristas list. Cannot remove {barista.name}")

           
    def sell_coffee(self, coffee_type, quantity):
       
        """
        The aim of this function is to sell the coffee making sure are the constraints are being considered.

        Notes:
        - Here I start by checking if there are sufficient ingredients for the quantity that is requested
            and if that's not the case I make sure it prompts the user to re-enter the quantity.
        - Similarly I check if there is enough labor capacity and prompt the user to re-enter if not the case.
        - After selling it updates the pantry quantities based on the ingredients needed and used for the sold coffee.
        - Updates the cash balance based on the revenue generated from the sale and updating the amount of time each barista worked.

        """

        demand = coffee_demand[coffee_type]

        # Calculating available capacity based on ingredient constraints
        availableingredients_cap = math.ceil(min(
            int(self.pantry['Milk'] / max(coffee_ingredients[coffee_type]['Milk'], 1)),
            int(self.pantry['Beans'] / max(coffee_ingredients[coffee_type]['Beans'], 1)),
            int(self.pantry['Spices'] / max(coffee_ingredients[coffee_type]['Spices'], 1)),
        ))  #using math.ceil to make sure its rounded to the next nearest integer as mentioned in spec

        availablelabor_cap = 0 if not self.baristas else min(
            max(0, math.ceil(barista.work_hours / coffee_preparation_time[coffee_type]))
            for barista in self.baristas
        )
        # Calculating the minimum available capacity and round it up to the nearest integer
        available_capacity = int(math.ceil(min(availableingredients_cap, availablelabor_cap)))

        # Check if available capacity is zero then print insufficient labor or ingredients
        while available_capacity == 0:
            print(f"Insufficient ingredients or labor to prepare {quantity} {coffee_type}. Available capacity: {available_capacity} cups.")
            quantity = 0
            break

#           Print available ingredients and prompt the user to re-enter the quantity
            print(f"Available Ingredients - {self.pantry}")
            new_quantity = int(input(f">>> Coffee {coffee_type}, demand {demand}, how much to sell (less than or equal to {math.ceil(available_capacity)}): ") or 0)
            quantity = min(new_quantity, demand)

            # Recalculate available capacity based on ingredient constraints
            availableingredients_cap = math.ceil(min(
                int(self.pantry['Milk'] / max(coffee_ingredients[coffee_type]['Milk'], 1)),
                int(self.pantry['Beans'] / max(coffee_ingredients[coffee_type]['Beans'], 1)),
                int(self.pantry['Spices'] / max(coffee_ingredients[coffee_type]['Spices'], 1)),
            ))

            # Recalculate available capacity based on labor constraints
            availablelabor_cap = float('inf') if not self.baristas else min(
                math.ceil(barista.work_hours / coffee_preparation_time[coffee_type]) if barista.work_hours > 0 else float('inf')
                for barista in self.baristas
            )


            # Recalculate the minimum available capacity and round it up to the nearest integer
            available_capacity = int(math.ceil(min(availableingredients_cap, availablelabor_cap)))


        # Calculate ingredients needed
        ingredients_needed = coffee_ingredients[coffee_type]

        # Check if there are enough ingredients
        while available_capacity == 0:
            print(f"Insufficient labor to prepare {quantity} {coffee_type}.")
            break
            while True:
                ingredients_sufficient = all(self.pantry[ingredient] >= quantity_needed * quantity for ingredient, quantity_needed in ingredients_needed.items())
                print(ingredients_sufficient)
                if ingredients_sufficient:
                    break
                else:
                    print(f"Insufficient ingredients for {quantity} {coffee_type}.")
                    print(f"Available Ingredients - {self.pantry}")

                    # Prompt the user to re-enter the quantity within the available capacity
                    rounded_capacity = math.ceil(available_capacity)
                    new_quantity = int(input(f">>> Coffee {coffee_type}, demand {demand}, how much to sell (less than or equal to {math.ceil(rounded_capacity):.0f}): ") or 0)
                    print("new_quantity: ", new_quantity)
                    print("new_quantity: ",new_quantity)
                    print("demand: ", demand)
                    quantity = min(new_quantity, demand)

   
        #Insufficient labor
       
        # Check if there is enough work hours for each barista
        total_work_hours = sum(barista.work_hours for barista in self.baristas)

        for barista in self.baristas:
            time_to_prepare = quantity * coffee_preparation_time[coffee_type]

            # Check if the barista has a specialty and it matches the current coffee type
            if barista.specialty and barista.specialty == coffee_type:
                time_to_prepare /= 2

            # Check if there are enough work hours left for this barista
            if time_to_prepare > barista.work_hours and barista.work_hours != 0 :
                availablelabor_cap = float('inf') if not self.baristas else min(
                    math.ceil(barista.work_hours / coffee_preparation_time[coffee_type]) if barista.work_hours > 0 else float('inf')
                    for barista in self.baristas
                )
                available_capacity = int(math.ceil(min(availableingredients_cap, availablelabor_cap)))
                print(f"Insufficient labor for {barista.name} to prepare {quantity} {coffee_type}. Available capacity: {available_capacity:.2f} cups")
               
                # Prompt the user to re-enter the quantity within the available capacity
                while True:
                    new_quantity = int(input(f">>> Coffee {coffee_type}, demand {demand}, how much to sell (up to {math.ceil(available_capacity):.2f}): ") or 0)
                    quantity = min(new_quantity, demand)

                    # Recalculate available capacity based on labor constraints
                    availablelabor_cap = float('inf') if not self.baristas else min(
                        math.ceil(barista.work_hours / coffee_preparation_time[coffee_type]) if barista.work_hours > 0 else float('inf')
                        for barista in self.baristas
                    )
                    availableingredients_cap = math.ceil(min(
                        int(self.pantry['Milk'] / max(coffee_ingredients[coffee_type]['Milk'], 1)),
                        int(self.pantry['Beans'] / max(coffee_ingredients[coffee_type]['Beans'], 1)),
                        int(self.pantry['Spices'] / max(coffee_ingredients[coffee_type]['Spices'], 1)),
                    ))
                
                    available_capacity = int(math.ceil(min(availableingredients_cap, availablelabor_cap)))
                
                    if 0 < quantity <= available_capacity:
                        break
        # Update pantry quantities
        self.update_pantry(ingredients_needed, quantity)

        # Display the results
        revenue = quantity * coffee_prices[coffee_type]
        self.cash_balance += revenue
        print(f"Sold {quantity} {coffee_type} for £{revenue:.2f}")
        print(f"Ingredients Left - {self.pantry}")

        # Print remaining work hours for each barista after selling each coffee type
        for barista in self.baristas:
            barista.prepare_coffee(coffee_type, quantity)
        print(f"Revenue from {coffee_type}: £{revenue:.2f}")

    def pay_baristas(self):
       
        """
        The function calculates the total payment required to pay all baristas based on their hourly rates and work hours.
       
        """
        total_payment = sum(barista.calculate_payment() for barista in self.baristas)
        self.cash_balance -= total_payment
        print(f"Paid baristas, total amount £{total_payment:.2f}")

    def pay_pantry_costs(self):
       
        """
        This function pays monthly costs for pantry maintenance, calculating costs depending on quantity
        and unit cost for each ingredient.

        """
        for ingredient, quantity in self.pantry.items():
            cost = abs(quantity * self.pantry_costs[ingredient])  # Use abs to ensure positive cost
            if cost > 0 and self.cash_balance >= cost:
                self.cash_balance -= cost
                print(f"Pantry {ingredient} cost £{cost:.2f}")
            elif cost > 0:
                print(f"Insufficient funds to pay {ingredient} cost. Need £{cost:.2f}, but only have £{self.cash_balance:.2f}")

    def display_status(self, end_of_month=True):
        """
        This function offers a quick overview of the coffee shop's financial and operational status,
        enabling owners to evaluate it.
        Shows coffee shop cash, pantry, and barista status.
       
        Args:
            end_of_month (bool, optional): If True, displays pantry information including depreciation at the end of the month.
                If False, displays pantry information without applying depreciation. Defaults to True.

        Notes:
        - The function prints the name of the coffee shop and its current cash balance.
        - If it's the end of the month, it displays information about each ingredient in the pantry, including quantities and capacities.
        - The function then prints information about each barista in the coffee shop, including their name, hourly rate, and specialty.

       
        """
        print(f"Shop Name: {self.name}, Cash: £{self.cash_balance:.2f}")

        # Display pantry information only at the end of the month
        if end_of_month:
            print(" Pantry")
            for ingredient, quantity in self.pantry.items():
                print(f" {ingredient}, {quantity:.2f} (capacity={pantry_capacity[ingredient]})")
        else:
            # Display pantry information without applying depreciation
            print(" Pantry")
            for ingredient, quantity in self.pantry.items():
                initial_quantity = pantry_capacity[ingredient]
                print(f" {ingredient}, {initial_quantity - self.pantry_depreciation[ingredient]:.2f} (capacity={initial_quantity})")

        # Display baristas information
        print(" Baristas")
        for barista in self.baristas:
            print(f" Barista {barista.name}, hourly rate={barista.hourly_rate}, Specialty: {barista.specialty}")


    def apply_depreciation(self):
       
        """
        Depreciation is applied to the ingredients that are stored in the pantry taking into account the pre-defined
        rates of depreciation that are mentioned in the spec.
.
        Notes:
        - The function depreciates each pantry ingredient at pre-defined rates.
            It calculates monthly depreciation for each ingredient using pantry quantity and depreciation rate.
        - It subtracts calculated depreciation from pantry quantity to avoid zero and prints.

        """
        for ingredient in self.ingredient_depreciation:
            # Calculate depreciation for the current month
            depreciation = math.ceil(self.pantry[ingredient] * self.ingredient_depreciation[ingredient])

            # Subtract depreciation from the pantry quantity
            self.pantry[ingredient] = max(0, self.pantry[ingredient] - depreciation)

            # Update pantry depreciation
            self.pantry_depreciation[ingredient] += depreciation

            # Display the depreciation for each ingredient
            print(f"Depreciated {depreciation:.2f} {ingredient}")

        # Display the updated pantry quantities after depreciation
        print(f"Ingredients Left after Depreciation - {self.pantry}")


    def restock_pantry(self):
       
        """
        This function restocks the pantry by purchasing ingredients from a supplier to reach full capacity.

        Notes:
        The function starts coffee shop pantry refilling.
        - It establishes a 'Supplier' class for ingredient purchases.
        Calculates pantry ingredient quantities to full capacity.
        Calls the 'Supplier' class's 'purchase_ingredients' function to get the needed quantities.
        Finally, it resets coffee shop baristas' work hours at the start of each month.

         """
        # Create a Supplier instance to handle ingredient purchases
        supplier = Supplier()
        # Calculate quantities needed to reach full capacity for each ingredient in the pantry
        quantities_needed = {ingredient: pantry_capacity[ingredient] - self.pantry[ingredient] for ingredient in self.pantry}
        supplier.purchase_ingredients(self, quantities_needed)

        # Reset the work hours for each barista at the beginning of the month
        for barista in self.baristas:
            barista.reset_capacity()

    def check_bankruptcy(self):
        """
        This function's goal is to give customers a quick way to assess the coffee shop's
        financial standing by looking at its cash balance.
        When the cash balance is negative or 0 shop goes bankrupt


        Notes:
        - The function checks if the coffee shop is bankrupt by examining its cash balance.
        - If the cash balance is less than 0, the function prints a message indicating that the shop went bankrupt and returns True.
        - If the cash balance is not negative, the function returns False, indicating that the shop is not bankrupt.

        """
        if self.cash_balance < 0:
            print(f"Shop went bankrupt! Cash balance: £{self.cash_balance:.2f}")
            return True
        return False

    def check_constraints(self, coffee_type, quantity, ingredients_needed, barista_time=None):
        """
        Checks if the constraints for selling a specified quantity of a certain coffee type are met.

        Args:
            coffee_type (str): The type of coffee to be sold.
            quantity (int): The quantity of coffee to be sold.
            ingredients_needed (dict): A dictionary representing the required ingredients and their quantities for the
            coffee.
            barista_time (float, optional): It calculates the time it takes for a barista to prepare one unit of the specified
            coffee type. If not provided, the default preparation time for the coffee type will be used.

        Returns:
            bool: This function will return True if all of the requirements are satisfied,
            which indicates that the coffee sale can go ahead.

        Notes:
        - Before permitting the sale of a particular quantity of coffee, the function performs a number of checks to
        ensure that it is not violating any constraints.
        -  An initial check is made to determine whether the quantity is greater than the demand for the particular
        variety of coffee.
        - It next determines whether or not there are sufficient quantities of the items in the pantry to meet the
        quantity that was requested.
        - Following that, it makes certain that there is at least one barista to ensure that the coffee is prepared.
        - It determines whether or not there are sufficient work hours for each barista to create the quantity that
        has been requested

        In addition to this, the function outputs informative messages for each constraint that is not met and returns
        False if any of the constraints are not met.
       
        """
       
        # Check if quantity exceeds demand
        demand = coffee_demand[coffee_type]
        if quantity > demand:
            print(f"Cannot sell {quantity} {coffee_type}. Exceeds demand ({demand})")
            return False

        # Check if there are enough ingredients
        for ingredient, quantity_needed in ingredients_needed.items():
            if self.pantry[ingredient] < quantity_needed * quantity:
                print(f"Insufficient {ingredient}: need {quantity_needed * quantity}, pantry {self.pantry[ingredient]:.2f}")
                return False

        # Check if there are any baristas
        if not self.baristas:
            print("No baristas available to prepare coffee.")
            return False

        # Check if there is enough work hours for each barista
        total_work_hours = sum(barista.work_hours for barista in self.baristas)

        for barista in self.baristas:
            time_to_prepare = quantity * (barista_time or coffee_preparation_time[coffee_type])

            # Check if the barista has a specialty and it matches the current coffee type
            if barista.specialty and barista.specialty == coffee_type:
                time_to_prepare /= 2

            print("barista.work_hours: ", barista.work_hours)
            print("coffee_preparation_time[coffee_type]: ", coffee_preparation_time[coffee_type])


        return True

    def update_pantry(self, ingredients_needed, quantity):
        """
        This function updates the pantry inventory based on the ingredients needed and the quantity of coffee prepared.

        Args:
            ingredients_needed (dict): A dictionary representing the required ingredients and their quantities.
                Example: {'coffee_beans': 50, 'milk': 200}
            quantity (int): The quantity of coffee to be prepared which is prompted by the user.


        Raises:
            ValueError: If the quantity is negative or if the ingredients_needed dictionary contains invalid data.

        """
        try:
            # Iterate through each ingredient and update the pantry inventory
            for ingredient, quantity_needed in ingredients_needed.items():
                new_quantity = self.pantry[ingredient] - quantity_needed * quantity
                # Ensure the updated quantity is not negative
                self.pantry[ingredient] = max(0, new_quantity)
        except KeyError as e:
            raise ValueError(f"Error updating pantry: Ingredient '{e}' not found in pantry.")
        except TypeError:
            raise ValueError("Error updating pantry: Invalid ingredients_needed format.")
        except ValueError as e:
            raise ValueError(f"Error updating pantry: {e}")

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

           
               



