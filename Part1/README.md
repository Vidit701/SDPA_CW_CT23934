# Simulation of a Coffee Shop Overview
This Coffee Shop Simulation is an interactive tool that tries to show how a coffee shop works in real life. It covers a lot of different areas, such as managing supplies, baristas, finances, and sales over a number of months chosen by the user. There are four main parts to the programme: the CoffeeShop, the Barista, the Supplier, and the main execution file.

# Organisation of Files
CoffeeShop.py: This file describes the CoffeeShop class, which handles cash flow, supplies, and barista tasks.
Barista.py: The file contains Barista class, which is in charge of the barista abilities and how they work.
Supplier.py: This file contains the Supplier class, which is what restocks the ingredients.
main.py: This is the main script for running the simulation. It lets users connect with and control the simulation.

# Setup
There is no need for external libraries to run this simulation. Make sure that Python 3.x is already installed on your computer.

# Executing the Simulation
It is important that all four files (Main.py, CoffeeShop.py, Barista.py, and Supplier.py) are in the same directory.
In the directory, you can get to a terminal or command prompt.
Run this command: python main.py
To simulate how the coffee shop works, follow the step-by-step directions.


# Let's look at each file to understand what each class and method is supposed to do.
## 1. CoffeeShop.py
This is the file that has the CoffeeShop class. The main part of the simulation is running the coffee shop. These are some important characteristics:
Attributes: It keeps track of the coffee shop's stock (pantry), cash flow, and schedule of baristas.

Functions: 
Add_barista(): A Barista is initialised with this function.
remove_barista(): This function is called to remove a barista from business.
Sell_coffee(): Coffee sales management and updating the cash balance and inventory are .
pay_baristas(): Calculates and pays Barista's salary from the available cash wallet.
pay_pantry_costs(): Deducts the price of the raw-material in the pantry.
display_status(): Gives the cash balance and inventory at any particular state.
Apply_depreciation(): Applies depreciation to the pantry items.
restock_pantry() Refills the pantry to full as per the quantity of items needed.
check_bankruptcy(): Defines weather the coffee shop goes bankrupt, not being able to pay bills and baristas.
check_constraints(): This function keeps an account of labour and inventory constraints, before selling coffee.
update_pantry(): After selling coffee, this function updates the pantry.

## 2. Barista.py
This file sets up the Barista class. The Barista class is in charge of the activities of making drinks in the coffee shop. Some important features are:
Attributes: Barista's name, specialty, wage, and working hours are initialised here.
Functions:
calculate_payment(): Defines the total salary of a Barista depending on the hourly wage.
reset_capacity(): This function refreshes the Barista's available working hours every month.
prepare_coffee(): The time taken to prepare the coffee is subtracted from the available working hours with this function.

## 3. Supplier.py
The Supplier class is contained in this file. The coffee shop needs to keep track of its stock, which can only be done with the Supplier class.
Features: Name of supplier and cost for each items are included.
Functons:
purchase_ingredients():Stores inventory, cash wallet and purchase from the supplier is managed by this function.

## 4. main.py
The primary script for the entire simulation is contained in this file. In this file, you'll find the main script for the whole game. Important traits include the following:
The simulation is coordinated by the main() file. After creating an instance of the CoffeeShop, it goes into a loop that lets the user manage baristas, sell coffee, and see the shop's status at the end of each month for a number of months that they can specify.


# Features
Interactive Control: The simulation can be personalised by adjusting the number of baristas and determining the amount of coffee sold.
Financial Management: Paying bills and salaries as well as calculating revenue along with inventory replenishments involves signigicant awareness.
Inventory Management: Keeping track of and restock coffee shop supplies such as milk, beans, and spices.
Coffee Sales Simulation: The actual feeling of running a coffee shop with real life situations makes it interesting.
Participation: I would encourage feedbacks and contributions to this project. Feel free to modify, and make pull requests.


