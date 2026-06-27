import random

class MenuItem:
    def __init__(self, starter, main, dessert):
        self.starter = starter
        self.main = main
        self.dessert = dessert


adminKey = "restaurant123"

dineInMenu = []
takeawayMenu = {}


def showDineInMenu():
    if len(dineInMenu) == 0:
        print("\nNo dine-in meals available.")
    else:
        print("\n===== DINE-IN MENU =====")
        for index, item in enumerate(dineInMenu, start=1):
            print(
                f"{index}. Starter: {item.starter} | Main: {item.main} | Dessert: {item.dessert}"
            )


def showTakeawayMenu():
    if len(takeawayMenu) == 0:
        print("\nNo takeaway foods available.")
    else:
        print("\n===== TAKEAWAY MENU =====")
        for itemNumber, foodItem in takeawayMenu.items():
            print(f"{itemNumber}. {foodItem}")


def customerDineIn():
    if len(dineInMenu) == 0:
        print("No dine-in meals available.")
        return

    tableNumber = input("Enter table number: ")

    if not tableNumber.isdigit() or int(tableNumber) <= 0:
        print("Invalid table number. Please enter a positive number.")
        return

    print(f"\nWelcome Table {tableNumber}")
    showDineInMenu()

    try:
        orderChoice = int(input("Enter the meal number you would like to order: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 1 <= orderChoice <= len(dineInMenu):
        selectedMeal = dineInMenu[orderChoice - 1]

        print("\n===== ORDER CONFIRMATION =====")
        print(f"Table Number: {tableNumber}")
        print(f"Starter: {selectedMeal.starter}")
        print(f"Main: {selectedMeal.main}")
        print(f"Dessert: {selectedMeal.dessert}")
        print("Your order has been sent to the kitchen.")
    else:
        print("Invalid meal number.")


def customerTakeaway():
    if len(takeawayMenu) == 0:
        print("No takeaway foods available.")
        return

    showTakeawayMenu()

    try:
        orderChoice = int(input("Enter the food number you would like to order: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if orderChoice in takeawayMenu:
        selectedFood = takeawayMenu[orderChoice]
        ticketNumber = random.randint(1000, 9999)

        print("\n===== ORDER CONFIRMATION =====")
        print(f"Ticket Number: {ticketNumber}")
        print(f"Food Item: {selectedFood}")
        print("Your takeaway order has been received and is being prepared.")
    else:
        print("Invalid food number.")


def manageDineInMenu():
    while True:
        print("\n===== MANAGE DINE-IN MENU =====")
        print("1. Add Meal")
        print("2. Show Meals")
        print("3. Update Meal")
        print("4. Delete Meal")
        print("5. Back")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid option.")
            continue

        if choice == 1:
            starter = input("Enter starter: ")
            main = input("Enter main: ")
            dessert = input("Enter dessert: ")

            if not starter.strip() or not main.strip() or not dessert.strip():
                print("All fields must be filled in. Meal not added.")
                continue

            dineInMenu.append(MenuItem(starter, main, dessert))
            print("Meal added successfully.")

        elif choice == 2:
            showDineInMenu()

        elif choice == 3:
            showDineInMenu()

            try:
                updateIndex = int(input("Enter meal number to update: ")) - 1
            except ValueError:
                print("Invalid input.")
                continue

            if 0 <= updateIndex < len(dineInMenu):
                newStarter = input(f"Enter new starter (current: {dineInMenu[updateIndex].starter}): ").strip()
                newMain = input(f"Enter new main (current: {dineInMenu[updateIndex].main}): ").strip()
                newDessert = input(f"Enter new dessert (current: {dineInMenu[updateIndex].dessert}): ").strip()

                if newStarter:
                    dineInMenu[updateIndex].starter = newStarter
                if newMain:
                    dineInMenu[updateIndex].main = newMain
                if newDessert:
                    dineInMenu[updateIndex].dessert = newDessert

                print("Meal updated successfully.")
            else:
                print("Invalid meal number.")

        elif choice == 4:
            showDineInMenu()

            try:
                deleteIndex = int(input("Enter meal number to delete: ")) - 1
            except ValueError:
                print("Invalid input.")
                continue

            if 0 <= deleteIndex < len(dineInMenu):
                confirm = input(f"Are you sure you want to delete '{dineInMenu[deleteIndex].main}'? (yes/no): ").lower()
                if confirm == "yes":
                    dineInMenu.pop(deleteIndex)
                    print("Meal deleted successfully.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid meal number.")

        elif choice == 5:
            break

        else:
            print("Invalid option.")


def manageTakeawayMenu():
    while True:
        print("\n===== MANAGE TAKEAWAY MENU =====")
        print("1. Add Food Item")
        print("2. Show Food Items")
        print("3. Remove Food Item")
        print("4. Sort Food Items")
        print("5. Back")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid option.")
            continue

        if choice == 1:
            foodItem = input("Enter food item: ").strip()

            if not foodItem:
                print("Food item cannot be empty.")
                continue

            itemNumber = max(takeawayMenu.keys(), default=0) + 1
            takeawayMenu[itemNumber] = foodItem
            print("Food item added successfully.")

        elif choice == 2:
            showTakeawayMenu()

        elif choice == 3:
            showTakeawayMenu()

            try:
                removeChoice = int(input("Enter food number to remove: "))
            except ValueError:
                print("Invalid input.")
                continue

            if removeChoice in takeawayMenu:
                confirm = input(f"Are you sure you want to remove '{takeawayMenu[removeChoice]}'? (yes/no): ").lower()
                if confirm == "yes":
                    removedItem = takeawayMenu.pop(removeChoice)
                    print(f"{removedItem} removed successfully.")
                else:
                    print("Removal cancelled.")
            else:
                print("Invalid food number.")

        elif choice == 4:
            sortedFoods = dict(sorted(takeawayMenu.items(), key=lambda item: item[1]))

            print("\n===== SORTED TAKEAWAY MENU =====")
            for itemNumber, foodItem in sortedFoods.items():
                print(f"{itemNumber}. {foodItem}")

        elif choice == 5:
            break

        else:
            print("Invalid option.")


running = True

while running:
    print("\n===== RESTAURANT AUTO CASHIER =====")
    print("1. Customer Dine-In Order")
    print("2. Customer Takeaway Order")
    print("3. Admin Dine-In Menu")
    print("4. Admin Takeaway Menu")
    print("5. Exit")

    try:
        mainChoice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid option.")
        continue

    if mainChoice == 1:
        customerDineIn()

    elif mainChoice == 2:
        customerTakeaway()

    elif mainChoice == 3:
        enteredKey = input("Enter admin key for dine-in menu: ")
        if enteredKey == adminKey:
            manageDineInMenu()
        else:
            print("Access denied.")

    elif mainChoice == 4:
        enteredKey = input("Enter admin key for takeaway menu: ")
        if enteredKey == adminKey:
            manageTakeawayMenu()
        else:
            print("Access denied.")

    elif mainChoice == 5:
        print("Thank you for using the system.")
        running = False

    else:
        print("Invalid option.")
