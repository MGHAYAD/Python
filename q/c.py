# Create a program that calculates the total cost of a meal at a restaurant, including tax and tip.
#  The user inputs the cost of the meal, the tax rate, and the tip percentage


# def calculate_total_cost(meal_cost, tax_rate, tip_percentage):
#     tax_amount = meal_cost * (tax_rate / 100)
#     tip_amount = meal_cost * (tip_percentage / 100)
#     total_cost = meal_cost + tax_amount + tip_amount
#     return total_cost

# def main():
#     try:
#         meal_cost = float(input("Enter the cost of the meal: $"))
#         tax_rate = float(input("Enter the tax rate (%): "))
#         tip_percentage = float(input("Enter the tip percentage (%): "))
        
#         total_cost = calculate_total_cost(meal_cost, tax_rate, tip_percentage)
        
#         print("Meal cost: ${:.2f}".format(meal_cost))
#         print("Tax amount: ${:.2f}".format(meal_cost * (tax_rate / 100)))
#         print("Tip amount: ${:.2f}".format(meal_cost * (tip_percentage / 100)))
#         print("Total cost: ${:.2f}".format(total_cost))
#     except ValueError:
#         print("Invalid input. Please enter valid numbers.")

# if __name__ == "__main__":
#     main()



# price_of_the_food =int(input('enter the price'))
# tax =float(input('enter the percentage'))
# tip =float(input('ente the amount'))
# total_price = price_of_the_food+tax+tip





price_of_the_food =int(input('enter the price'))
tax = price_of_the_food * 2.5 / 100
tip =float(input('ente the amount'))
total_price = price_of_the_food+tax+tip

print(total_price)
print(tax)
