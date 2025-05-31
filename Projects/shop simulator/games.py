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

# Initialize selling prices (default to 0). These will be the prices you SELL at.
bp = 0 # Selling price for bread
mp = 0 # Selling price for milk
icp = 0 # Selling price for ice cream
up = 0 # Selling price for umbrellas

ask = input("play a game?:")

if ask == "yes":
    while True:
        print(f'\n--- Current Status ---')
        print(f'Your Money: ${money}')
        print(f'Current Stock: Bread={bread_food}, Milk={milk_food}, Ice Cream={ice_cream_food}, Umbrellas={umbrellathing}')
        print(f'Current Selling Prices: Bread=${bp}, Milk=${mp}, Ice Cream=${icp}, Umbrellas=${up}') # Display current selling prices
        print(f'----------------------')

        ask_food_str = input("1.bread\n2.milk\n3.ice cream\n4.umbrella\n5.done\nchoose:")

        if not ask_food_str.isdigit():
            print("Invalid input. Please enter a number from 1 to 5.")
            continue # Go back to the start of the while loop

        ask_food = int(ask_food_str)

        if ask_food == 1:
            print(f"Bread buying price: ${breaddollar}")
            breadask = int(input("How much bread?:"))
            cost = breaddollar * breadask
            if money >= cost: # Check if enough money
                bread_food += breadask
                money -= cost
                print(f"You bought {breadask} bread for ${cost}. Total bread={bread_food}")
                new_bp = int(input(f"Enter a NEW selling price for ALL bread (current: ${bp}):"))
                bp = new_bp # Update the selling price for ALL bread
                print(f"Selling price for ALL bread is now set to ${bp}.")
            else:
                print("Not enough money to buy that much bread!")
        elif ask_food == 2:
            print(f"Milk buying price: ${milkdollar}")
            milk_food_bought = int(input("How much milk?: "))
            cost = milkdollar * milk_food_bought
            if money >= cost:
                milk_food += milk_food_bought
                print(f"You bought {milk_food_bought} milk for ${cost}. Total milk={milk_food}")
                new_mp = int(input(f"Enter a NEW selling price for ALL milk (current: ${mp}):"))
                mp = new_mp
                print(f"Selling price for ALL milk is now set to ${mp}.")
                money -= cost
            else:
                print("Not enough money to buy that much milk!")
        elif ask_food == 3:
            print(f"Ice Cream buying price: ${i_cdollar}")
            ice_cream_food_bought = int(input("How much ice cream?: "))
            cost = i_cdollar * ice_cream_food_bought
            if money >= cost:
                ice_cream_food += ice_cream_food_bought
                print(f"You bought {ice_cream_food_bought} ice cream for ${cost}. Total ice-cream={ice_cream_food}")
                new_icp = int(input(f"Enter a NEW selling price for ALL ice cream (current: ${icp}):"))
                icp = new_icp
                print(f"Selling price for ALL ice cream is now set to ${icp}.")
                money -= cost
            else:
                print("Not enough money to buy that much ice cream!")
        elif ask_food == 4:
            print(f"Umbrella buying price: ${umbrelladollar}")
            umbrellathing_bought = int(input("How many umbrellas?: "))
            cost = umbrelladollar * umbrellathing_bought
            if money >= cost:
                umbrellathing += umbrellathing_bought
                print(f"You bought {umbrellathing_bought} umbrellas for ${cost}. Total umbrella={umbrellathing}")
                new_up = int(input(f"Enter a NEW selling price for ALL umbrellas (current: ${up}):"))
                up = new_up
                print(f"Selling price for ALL umbrellas is now set to ${up}.")
                money -= cost
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

            # Variables to store the day's demand (useful for debugging)
            pbbread_demand = 0
            pbmilk_demand = 0
            pbic_demand = 0
            pbu_demand = 0

            if day == 1:
                days = "sunny"
                pbbread_demand = randint(5, 25)
                pbmilk_demand = randint(5, 35)
                pbic_demand = randint(5, 65)
                pbu_demand = randint(5, 10)
                print(f"\nIt's a {days} day!")

            elif day == 2:
                days = "rainy"
                pbbread_demand = randint(5, 25)
                pbmilk_demand = randint(5, 30)
                pbic_demand = randint(5, 15)
                pbu_demand = randint(10, 100)
                print(f"\nIt's a {days} day!")

            # --- Consumption Logic (applies to both day types) ---
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

            # Ensure stocks are not negative (redundant with min(), but safe)
            bread_food = max(0, bread_food)
            milk_food = max(0, milk_food)
            ice_cream_food = max(0, ice_cream_food)
            umbrellathing = max(0, umbrellathing)

            # --- Earnings Calculation ---
            money_earned_bread = actual_bread_consumed * bp
            money_earned_milk = actual_milk_consumed * mp
            money_earned_ic = actual_ic_consumed * icp
            money_earned_umbrella = actual_umbrella_consumed * up

            money += money_earned_bread
            money += money_earned_milk
            money += money_earned_ic
            money += money_earned_umbrella

            print("\n--- Day's Consumption & Sales Report ---")
            print(f"Bread: Demand={pbbread_demand}, Consumed={actual_bread_consumed}, Earned=${money_earned_bread} (at ${bp}/unit)")
            print(f"Milk: Demand={pbmilk_demand}, Consumed={actual_milk_consumed}, Earned=${money_earned_milk} (at ${mp}/unit)")
            print(f"Ice Cream: Demand={pbic_demand}, Consumed={actual_ic_consumed}, Earned=${money_earned_ic} (at ${icp}/unit)")
            print(f"Umbrellas: Demand={pbu_demand}, Consumed={actual_umbrella_consumed}, Earned=${money_earned_umbrella} (at ${up}/unit)")
            print(f"Your total money after sales: ${money}")

            # Check for game end conditions
            if money <= 0:
                print("\nYou ran out of money! Game Over!")
                break # Exit the main game loop

            x = input("Continue to next day? (yes/no):").lower()
            if x == "no":
                print("Exiting game.")
                break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

else:
    print("Okay, maybe next time!")

print("\n--- Game Over ---")
print(f"Final Money: ${money}")
print(f"Final Stock: Bread={bread_food}, Milk={milk_food}, Ice Cream={ice_cream_food}, Umbrellas={umbrellathing}")