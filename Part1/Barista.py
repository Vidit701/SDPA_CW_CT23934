coffee_demand = {'Espresso': 500, 'Americano': 200, 'Filter': 300, 'Macchiato': 400, 'Flat White': 600, 'Latte': 1000}
coffee_prices = {'Espresso': 1.5, 'Americano': 2.5, 'Filter': 1.5, 'Macchiato': 3.0, 'Flat White': 3.5, 'Latte': 4.0}
coffee_ingredients = {'Espresso': {'Milk': 0.0, 'Beans': 8, 'Spices': 0}, 'Americano': {'Milk': 0.0, 'Beans': 6, 'Spices': 0},
                      'Filter': {'Milk': 0.0, 'Beans': 4, 'Spices': 0}, 'Macchiato': {'Milk': 0.1,'Beans': 8, 'Spices': 2},
                      'Flat White': {'Milk': 0.2, 'Beans': 8, 'Spices': 1}, 'Latte': {'Milk': 0.3, 'Beans': 8, 'Spices': 3}}
coffee_preparation_time = {'Espresso': 0.05, 'Americano': 0.0333, 'Filter': 0.0167, 'Macchiato': 0.0667,
                           'Flat White': 0.0833,
                           'Latte': 0.1}
import math

# Define pantry capacities
pantry_capacity = {'Milk': 300, 'Beans': 20000, 'Spices': 4000}

class Barista:
    
    """"
    This class is a representation of a barista who is paid on an hourly basis and is responsible for preparing coffee.
    
    """
    
    def __init__(self, name, hourly_rate, specialty=None):
        
        """
        Initializes a new Barista instance.
        
        Args:
            name (str): The name of the barista.
            hourly_rate (float): The hourly rate at which the barista is paid default .
            specialty (str, optional): refers to the type of speciality coffee that the barista is familiar with and talented at making. Sets to None by default.
        
        Raises:
            ValueError: If there is an issue with the input values (e.g., invalid hourly rate).

        Returns:
            None
        """
        
        try:
            self.name = name
            self.hourly_rate = float(hourly_rate)  # Convert to float to handle non-integer input
            self.specialty = specialty.lower() if specialty else None  # Convert to lowercase if not None
            self.work_hours = 80
            
        except ValueError as e:
            raise ValueError(f"Error creating Barista: {e}")

    def calculate_payment(self):
        """
        Aim of this function is to calculate the monthly payment for the barista based on the hourly rate and a fixed monthly work hours.
        Each barista is being paid at an hourly_rate of 15£  per month irrespective of the demand
        
        Args:
            None

        Returns:
            float: The calculated monthly payment for the barista.
        """
    
        return 120 * self.hourly_rate

    def reset_capacity(self):
        """
        This function resets the remaining work hours of the barista to the default value (80) at the start of each month.
        Setting maximum working hours for each barista to 80
        Args:
            None

        Returns:
            None
        """
        
        self.work_hours = 80  

        
    def prepare_coffee(self, coffee_type, quantity):
        
        
        time_to_prepare = quantity * coffee_preparation_time[coffee_type]

        # Check if the barista has a specialty and it matches the current coffee type
        if self.specialty and self.specialty == coffee_type:
            time_to_prepare /= 2

        # Update the remaining work hours
        self.work_hours = max(0, self.work_hours - time_to_prepare)
        
        if self.work_hours == 0:
            print(f"{self.name} has no remaining work hours.")
        else:
            available_capacity = math.ceil(self.work_hours / coffee_preparation_time[coffee_type])