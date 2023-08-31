# Write a program that asks the user for their current speed while driving and checks if they are exceeding the speed limit 
# (e.g., 60 mph). If they are, it prints a message indicating they are speeding. 



   

# Get user's current speed
user_speed = float(input("Enter your current speed (in mph): "))

# Check if user is speeding
if user_speed > 60:
    print("You are speeding! Slow down.")
else:
    print("You are within the speed limit. Drive safely.")
