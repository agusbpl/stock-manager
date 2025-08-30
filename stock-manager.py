print("welcome to the ultimate gen stock manager 0.0.1")
print("-----------------------------------------------")
print("\n\nplease select one of the following options to start the stock-management")


inventory = {}


options = ("\n[a]dd","[d]elete","[s]how inventory","[c]ancel")

while True:
    for opt in options:
        print(opt)
    user_choice = input("\nyour selection: ")
    if not (user_choice in ["a","d","s","c"]):
        print("invalid response")
        exit(1)
    elif user_choice == "a":
        product_name = input("name: ")
        product_weight = int(input("weight: "))
        inventory.update({product_name:product_weight})
        print(f"\n{product_name} added succesfuly")
    elif user_choice == "d":
        product_name = input("producto a eliminar: ")
        inventory.pop({product_name})
        print(f"{product_name} deleted succesfuly")
    elif user_choice == "s":
        print("\nshowing inventory")
        for num,(prod_name,prod_weight) in enumerate(inventory.items()):
            print(f"    {num + 1}. {prod_name} {prod_weight/ 1000} kg")
    else:
        print("exiting")
        exit(1)
        