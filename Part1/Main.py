# Creating dictionaries for all the pre-stated units from the spec

coffee_demand = {'Espresso': 500, 'Americano': 200, 'Filter': 300, 'Macchiato': 400, 'Flat White': 600, 'Latte': 1000}
coffee_prices = {'Espresso': 1.5, 'Americano': 2.5, 'Filter': 1.5, 'Macchiato': 3.0, 'Flat White': 3.5, 'Latte': 4.0}
coffee_ingredients = {'Espresso': {'Milk': 0.0, 'Beans': 8, 'Spices': 0}, 'Americano': {'Milk': 0.0, 'Beans': 6, 'Spices': 0},
                      'Filter': {'Milk': 0.0, 'Beans': 4, 'Spices': 0}, 'Macchiato': {'Milk': 0.1,'Beans': 8, 'Spices': 2},
                      'Flat White': {'Milk': 0.2, 'Beans': 8, 'Spices': 1}, 'Latte': {'Milk': 0.3, 'Beans': 8, 'Spices': 3}}
coffee_preparation_time = {'Espresso': 0.05, 'Americano': 0.0333, 'Filter': 0.0167, 'Macchiato': 0.0667,
                           'Flat White': 0.0833,
                           'Latte': 0.1}
pantry_capacity = {'Milk': 300, 'Beans': 20000, 'Spices': 4000}

from CoffeeShop import CoffeeShop # importing the CoffeeShop class from the file so that we can use all the functions from that class
def main():
    """
    The main function makes sure that the outputs of the simulation are called by using the functions from CoffeeShop class.
    There are several things that we are prompting from the user like:
    - Entering the number of months to simulate from the user.
    Here I make sure that the even if the user presses enter the default of 6 months is taken into consideration
    and it outputs value error in cases where int is not provided.
    - Adding and removing baristas in accordance with user input ensuring case sensitivity issues are taken into consideration.
    Additionally, in the first month the user cannot input a negative number as no Barista has been initialized 
    and we cannot remove all the baristas from the shop it would prompt an error message and stop the user from doing it making sure 
    atleast one barista is present.
    -Hourly wage if not given, would be considered as 15/hr.
    - Handling inventory and selling coffee and taking care of monthly finances, including rent, utilities, barista salaries.
    - Verifying bankruptcy status.
    - Showcasing the coffee shop in its finished state.

    """
    try:
        # Prompting the user to enter the months
        num_months = int(input("Please enter the number of months (press Enter to consider the default months (6)): ") or 6)

        #hereonwards shop would be considered as the CoffeeShop class
        shop = CoffeeShop()
        
        for month in range(1, num_months + 1):
            print("=" * 32)
            print(f"====== SIMULATING month {month} ======")
            print("=" * 32)

            shop.restock_pantry()

            # Adding and removing baristas, sell coffee, and update shop status for the months
            while True:
                try:
                    num_baristas_input = input("To add, enter a positive number. To remove, enter a negative number. For no change, press Enter.\n>>> Enter the number of baristas: ")
                    if not num_baristas_input.strip():  # Check if input is empty (pressing Enter)
                        num_baristas = 0
                        break
                    num_baristas = int(num_baristas_input)
                    if num_baristas > 0:
                        if 0 <= num_baristas <= (shop.max_baristas - len(shop.baristas)):
                            break
                        else:
                            print(f"Invalid input. You can add up to {shop.max_baristas - len(shop.baristas)} baristas.")
                    elif num_baristas < 0:
                        if abs(num_baristas) <= len(shop.baristas):
                            break
                        else:
                            print(f"Invalid input. You can remove up to {len(shop.baristas)} baristas.")
                    else:
                        print("Invalid input. Please enter a non-zero integer.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            if num_baristas > 0:
                for _ in range(num_baristas): #Barista names have been converted to lower string to avoid multiple same names
                    name = input(">>> Enter barista name: ")
                    already_exists_baristas= [barista.name.lower() for barista in shop.baristas]
                    while name.lower() in already_exists_baristas:
                        print(f"A barista with the name '{name}' already exists. Please enter a different name.")
                        name = input("Enter a new barista name: ")

                    hourly_rate_input = input(f"Enter hourly rate for {name} (press Enter to use the default): ")

                    if hourly_rate_input.strip():  # Check if input is not empty, default rate is 15/hr
                        try:
                            hourly_rate = float(hourly_rate_input)
                        except ValueError:
                            print("Invalid input. Using the default hourly rate of 15.")
                            hourly_rate = 15  # default is taken as 15 hours 
                    else:
                        hourly_rate = 15
                        
                    specialty_input = input(f"Does {name} have a specialty? (yes/no): ")
                    specialty = None
                    if specialty_input.strip().lower() == 'yes':
                        coffee_type = input(f"Enter the coffee type {name} specializes in: ")
                        specialty = coffee_type

                    shop.add_barista(name, hourly_rate, specialty)

            elif num_baristas < 0:
                # Removing baristas can be done from second month
                for _ in range(abs(num_baristas)):
                    name = input(">>> Enter barista name to remove: ")
                    already_exists_baristas= [barista.name.lower() for barista in shop.baristas] # converting to lower case for case sensitive issue
                    while name.lower() not in already_exists_baristas:
                        print(f"No barista with the name '{name}' exists. Please enter a valid name.")
                        name = input("Enter a valid barista name to remove: ")

                    barista_to_remove = next(barista for barista in shop.baristas if barista.name == name)
                    shop.remove_barista(barista_to_remove)
                   
            for coffee_type, demand in coffee_demand.items():
                while True:
                    quantity_input = input(f">>> Coffee {coffee_type}, demand {demand}, how much to sell (less than or equal to {demand}): ")
                    if not quantity_input:
                        print("Please enter a quantity.")
                        continue

                    try:
                        quantity = int(quantity_input)
                        if 0 <= quantity <= demand:  # Allow 0 as a valid quantity
                            break
                        else:
                            print(f"Invalid quantity. Please enter a quantity between 0 and {demand}.")
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

                if quantity == 0:
                    continue  # Skip the sale calculation for 0 quantity

                shop.sell_coffee(coffee_type, quantity)

            # Calling the functions to sell the coffee followed by calculating the bank balance of the coffee shop
            shop.pay_baristas()
            shop.pay_pantry_costs()
            shop.cash_balance -= shop.rent_utilities_cost
            print(f"Rent and utilities paid: £{shop.rent_utilities_cost:.2f}")
            shop.display_status()

            # Apply depreciation, restock pantry, and check bankruptcy
            shop.apply_depreciation()

            if shop.check_bankruptcy():
                print(f"Went bankrupt in month {month}")  #ending the simulation once the shop got bankrupt
                break

        # Display the final state of the shop
        print(f"=== FINAL STATE month {month} ===")
       
        shop.display_status()

    except ValueError as e: # adding value errors to avoid any discrepancy
        print(f"Error: {e}. Please enter a valid number of months.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

