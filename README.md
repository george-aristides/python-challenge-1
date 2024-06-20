# Food Truck Order System

## Description

This script lets you order from my food truck! You can run through it and choose as many or as few of any item as you like, and see an itemized receipt at the end with your total.

## How to Use

1. **Run the Script**: Execute the script to start the ordering process.

2. **Select a Menu Category**: Choose a category from Snacks, Meals, Drinks, or Desserts by typing the corresponding number.

3. **Select an Item**: Within the chosen category, select an item by typing its number.

4. **Specify Quantity**: Enter the desired quantity of the selected item.

5. **Continue or Complete Order**: Decide whether to continue ordering or to complete the order.

6. **Review Order**: Once the order is complete, the script will display a summary of all items ordered along with their prices and quantities, and calculate the total cost.

## Features

- **User-Friendly Interface**: Guides the user through selecting categories and items.
- **Validation**: Ensures that the user inputs valid numbers for menu selections and quantities.
- **Order Summary**: Provides a clear and formatted summary of the order.

## Example

```text
Welcome to the variety food truck.
From which menu would you like to order? 
1: Snacks
2: Meals
3: Drinks
4: Dessert
Type menu number: 2
You selected Meals
What Meals item would you like to order?
Item # | Item name                | Price
-------|--------------------------|-------
1      | Burrito - Beef           | $7.99
2      | Burrito - Chicken        | $8.99
3      | Burrito - Bean           | $6.99
4      | Pizza - Cheese           | $8.99
5      | Pizza - Pepperoni        | $10.99
6      | Pizza - Vegetarian       | $9.99
7      | Gyro - Chicken           | $7.49
8      | Gyro - Pork              | $8.49
Type menu item number: 1
How many Burrito - Beef would you like to order? 2
Would you like to keep ordering? (Y)es or (N)o y
...
Would you like to keep ordering? (Y)es or (N)o n
This is what we are preparing for you.

Item name                 | Price  | Quantity
--------------------------|--------|----------
Burrito - Beef            | $7.99  | 2

Total price: $15.98
