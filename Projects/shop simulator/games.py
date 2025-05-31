from random import randint
import time

breaddollar = 3 # Buying price
milkdollar = 2
i_cdollar = 4
umbrelladollar = 8
money = 1000

# Initialize food/item stocks and selling prices BEFORE the loop
bread_food = 0
milk_food = 0
ice_cream_food = 0
umbrellathing = 0

# Initialize selling prices (default to 0 or some base if not set by user)
# Or, you could make them fixed here if they don't change based on user input
bp = 0
mp = 0
icp = 0
up = 0

ask = input("play a game?:")

if ask == "yes":
    while True:
        print(f'\n--- Current Status ---')
        print(f'Your Money: ${money}')
        print(f'Current Stock: Bread={bread_food}, Milk={milk_food}, Ice Cream={ice_cream_food}, Umbrellas={umbrellathing}')
        print(f'----------------------')

        ask_food_str = input("1.bread\n2.milk\n3.ice cream\n4.umbrella\n5.done\nchoose:")

        if not ask_food_str.isdigit():
            print("Invalid input. Please enter a number from 1 to 5.")
            continue # Go back to the start of the while loop

        ask_food = int(ask_food_str)

        if ask_food == 1:
            print(f"Bread buying price: ${breaddollar}")
            breadask = int(input("How much bread?:"))
            if money >= (breaddollar * breadask): # Check if enough money
                bread_food += breadask
                money -= (breaddollar * breadask)
                print(f"You bought {breadask} bread. Total bread={bread_food}")
                bp = int(input("Enter a selling price for bread:")) # Set selling price for bread
            else:
                print("Not enough money to buy that much bread!")
        elif ask_food == 2:
            print(f"Milk buying price: ${milkdollar}")
            milk_food_bought = int(input("How much milk?: "))
            if money >= (milkdollar * milk_food_bought):
                milk_food += milk_food_bought
                print(f"You bought {milk_food_bought} milk. Total milk={milk_food}")
                mp = int(input("Enter a selling price for milk:")) # Set selling price for milk
                money -= (milkdollar * milk_food_bought)
            else:
                print("Not enough money to buy that much milk!")
        elif ask_food == 3:
            print(f"Ice Cream buying price: ${i_cdollar}")
            ice_cream_food_bought = int(input("How much ice cream?: "))
            if money >= (i_cdollar * ice_cream_food_bought):
                ice_cream_food += ice_cream_food_bought
                print(f"You bought {ice_cream_food_bought} ice cream. Total ice-cream={ice_cream_food}")
                icp = int(input("Enter a selling price for ice cream:")) # Set selling price
                money -= (i_cdollar * ice_cream_food_bought)
            else:
                print("Not enough money to buy that much ice cream!")
        elif ask_food == 4:
            print(f"Umbrella buying price: ${umbrelladollar}")
            umbrellathing_bought = int(input("How many umbrellas?: "))
            if money >= (umbrelladollar * umbrellathing_bought):
                umbrellathing += umbrellathing_bought
                print(f"You bought {umbrellathing_bought} umbrellas. Total umbrella={umbrellathing}")
                up = int(input("Enter a selling price for umbrellas:")) # Set selling price
                money -= (umbrelladollar * umbrellathing_bought)
            else:
                print("Not enough money to buy that many umbrellas!")
        elif ask_food == 5:
            print("\n--- Advancing to Next Day ---")
            time.sleep(3)
            day = randint(1, 2)

            # Variables to store actual consumption for selling purposes
            actual_bread_consumed = 0
            actual_milk_consumed = 0
            actual_ic_consumed = 0
            actual_umbrella_consumed = 0

            if day == 1:
                days = "sunny"
                pbbread_demand = randint(5, 25)
                pbmilk_demand = randint(5, 35)
                pbic_demand = randint(5, 65)
                pbu_demand = randint(5, 10)
                print(f"\nIt's a {days} day!")

                # Cap demand at available stock BEFORE deduction
                actual_bread_consumed = min(pbbread_demand, bread_food)
                actual_milk_consumed = min(pbmilk_demand, milk_food)
                actual_ic_consumed = min(pbic_demand, ice_cream_food)
                actual_umbrella_consumed = min(pbu_demand, umbrellathing)

                # Deduct consumption
                bread_food -= actual_bread_consumed
                milk_food -= actual_milk_consumed
                ice_cream_food -= actual_ic_consumed
                umbrellathing -= actual_umbrella_consumed

                # Report if out of stock
                if bread_food <= 0 and pbbread_demand > 0: # Check if demand existed
                    print("Out of bread.")
                if milk_food <= 0 and pbmilk_demand > 0:
                    print("Out of milk.")
                if ice_cream_food <= 0 and pbic_demand > 0:
                    print("Out of ice-cream.")
                if umbrellathing <= 0 and pbu_demand > 0:
                    print("Out of umbrellas.")


            elif day == 2: # This block is now correctly indented
                days = "rainy"
                pbbread_demand = randint(5, 25)
                pbmilk_demand = randint(5, 30)
                pbic_demand = randint(5, 15)
                pbu_demand = randint(10, 100)
                print(f"\nIt's a {days} day!")

                # Cap demand at available stock BEFORE deduction
                actual_bread_consumed = min(pbbread_demand, bread_food)
                actual_milk_consumed = min(pbmilk_demand, milk_food)
                actual_ic_consumed = min(pbic_demand, ice_cream_food)
                actual_umbrella_consumed = min(pbu_demand, umbrellathing)

                # Deduct consumption
                bread_food -= actual_bread_consumed
                milk_food -= actual_milk_consumed
                ice_cream_food -= actual_ic_consumed
                umbrellathing -= actual_umbrella_consumed

                # Report if out of stock
                if bread_food <= 0 and pbbread_demand > 0:
                    print("Out of bread.")
                if milk_food <= 0 and pbmilk_demand > 0:
                    print("Out of milk.")
                if ice_cream_food <= 0 and pbic_demand > 0:
                    print("Out of ice-cream.")
                if umbrellathing <= 0 and pbu_demand > 0:
                    print("Out of umbrellas.")

            # Ensure stocks are not negative (though min() should prevent this if always used)
            bread_food = max(0, bread_food)
            milk_food = max(0, milk_food)
            ice_cream_food = max(0, ice_cream_food)
            umbrellathing = max(0, umbrellathing)


            # Calculate money gained from selling consumed items
            # Use the 'actual_consumed' values and the set selling prices
            money += actual_bread_consumed * bp
            money += actual_milk_consumed * mp
            money += actual_ic_consumed * icp
            money += actual_umbrella_consumed * up

            print(f"Your money after selling: ${money}")

            # Check for game end conditions
            if money <= 0:
                print("\nYou ran out of money! Game Over!")
                break # Exit the main game loop

            x = input("Continue to next day? (yes/no):").lower() # Use .lower() for flexible input
            if x == "no":
                print("Exiting game.")
                break # Exit the main game loop

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

else:
    print("Okay, maybe next time!")

print("\n--- Game Over ---")
print(f"Final Money: ${money}")
print(f"Final Stock: Bread={bread_food}, Milk={milk_food}, Ice Cream={ice_cream_food}, Umbrellas={umbrellathing}")