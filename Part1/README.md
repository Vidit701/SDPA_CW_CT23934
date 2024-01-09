# Simulation of a Coffee Shop Overview
This Coffee Shop Simulation is an interactive programme developed in Python that aims to replicate the day-to-day operations of a coffee shop. It includes a wide range of topics like inventory management, barista management, financial operations, and sales over a user-defined number of months. The programme is divided into four main components: CoffeeShop, Barista, Supplier, and the main execution script.


# Organisation of Files
CoffeeShop.py: Introduces the CoffeeShop class that manages inventory, cash flow, and barista operations.
Barista.py: Includes the Barista class, responsible for handling barista attributes and their operations.
Supplier.py: Implements the Supplier class, which handles the task of replenishing ingredients.
main.py: The primary script for running the simulation, providing users with the ability to interact with and control the simulation.
Setup
This simulation can be run without the need for any external libraries. Make sure Python 3.x is installed on your system.

# Executing the Simulation
Make sure that all four files (CoffeeShop.py, Barista.py, Supplier.py, main.py) are located in the same directory.
Access a terminal or command prompt within this directory.
Execute the command: python main.py
Follow the step-by-step instructions to simulate the coffee shop's operations.

Let us examine each of the files (CoffeeShop.py, Barista.py, Supplier.py, and main.py) and elucidate the intent behind each class and function.

## 1. CoffeeShop.py
The CoffeeShop class is contained in this file. Managing the coffee shop's operations forms the basis of your simulation. Important characteristics consist of:

Features: Keeps track of the coffee shop's inventory (pantry), cash balance, and barista roster.

Techniques:
Add_barista(): Enables the shop to hire a new barista.
remove_barista(): Takes a barista out of business.
Sell_coffee() manages the coffee sale process and updates the cash balance and inventory.
pay_baristas() computes and subtracteds each barista's salary from the available cash.
pay_pantry_costs() subtracts the price of the goods in the pantry.
display_status(): Shows the coffee shop's current state, including its finances and inventory.
Apply_depreciation(): This function gives the inventory items a depreciation.
restock_pantry() replenishes the pantry contents by making purchases from the vendor.
check_bankruptcy(): Determines whether the coffee shop is in bankruptcy.
check_constraints() verifies a number of constraints, including labour and inventory constraints, before selling coffee.
After selling coffee, the update_pantry() function updates the pantry.
update_pantry(): Following the sale of coffee, updates the pantry.

## 2. Barista.py
The Barista class is defined in this file. Representing the workers in the coffee shop is the responsibility of the Barista class. Important features consist of:

Attributes: Contains the name, specialty, hourly fee, and work hours that the barista is available for.
Techniques:
calculate_payment(): Determines the barista's total payment amount based on their hourly wage.
reset_capacity(): Once called at the beginning of each month, this function resets the barista's available work hours.
prepare_coffee(): Subtracts from the barista's available labour hours the amount of time required to prepare coffee.


## 3. Supplier.py
The Supplier class is contained in this file. The coffee shop's inventory must be managed, and this requires the Supplier class. Important characteristics consist of:
Features: Name of supplier and cost for each items are included.
Techniques:
purchase_ingredients(): Manages the supplier's ingredient purchases, keeping track of the store's inventory and cash balance.

## 4. main.py
The primary script for the entire simulation is contained in this file. It includes your program's entry point, the main() function, and imports the CoffeeShop, Barista, and Supplier classes. Important characteristics consist of:

The simulation is coordinated by the main() method. After creating an instance of the CoffeeShop, it goes into a loop that lets the user manage baristas, sell coffee, and see the shop's status at the end of each month for a number of months that they can specify.


# Features
Interactive Control: Personalise the simulation by adjusting the number of baristas and determining the amount of coffee sold.
Financial Management: Keep a close eye on the shop's cash balance, making sure to carefully monitor expenses for inventory and salaries.
Inventory Management: Keep track of and restock coffee shop supplies such as milk, beans, and spices.
Coffee Sales Simulation: Experience the thrill of simulating sales in the coffee industry, where you'll navigate through fluctuating demand and limited resources.
Participating
We encourage feedback and contributions to this project. Feel free to fork, modify, and make pull requests or open issues for any suggestions or problems.


