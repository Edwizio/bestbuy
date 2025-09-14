import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store_obj):
    """
    This function prints the menu and provides user interface for the user to buy and order stuff.
    :param store_obj:
    """
    while True:
        print("\n--- Welcome to the Store ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "4":
            print("Thank you for visiting!")
            break

        elif choice == "1":
            print("\nProducts in store:")
            for product in store_obj.get_all_products():
                print(product.show())

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print("\nTotal items in store: " + str(total_quantity))

        elif choice == "3":
            shopping_list = []

            print("\nProducts available:")
            for product in store_obj.get_all_products():
                print(product.show())

            while True:
                product_name = input("When you want to finish order, enter empty text.\nWhich product # do you want? ")
                if product_name == " ":
                    break

                try:
                    product_number = int(product_name)
                    if product_number < 1 or product_number > len(product_list):
                        print("Please choose a valid product number.")
                        continue

                    selected_product = product_list[product_number - 1]
                    quantity_input = input("Enter quantity for " + selected_product.name + ": ").strip()
                    quantity = int(quantity_input)
                    shopping_list.append((selected_product, quantity))

                except:
                    print("Please enter a valid number.")

            if shopping_list:
                try:
                    total_cost = store_obj.order(shopping_list)
                    print("\nOrder completed! Total cost: " + str(total_cost) + " dollars.")
                except Exception as e:
                    print("Error processing order:", e)

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")

start(best_buy)
