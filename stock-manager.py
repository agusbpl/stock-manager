print("welcome to the ultimate gen stock manager 0.0.1")
print("-----------------------------------------------")
print("\n\nplease select one of the following options to start the stock-management")


inventory = {}


options = ("[a]dd","[d]elete","[s]how inventory","[c]ancel")

while True:
    for opt in options:
        print(opt)
    user_choice = input("your selection: ")
    if not (user_choice in ["a","d","s","c"]):
        print("invalid response")
        exit(1)
    elif user_choice == "a":
        product_name = input("name: ")
        product_weight = input("weight: ")
        inventory.update({product_name:product_weight})
        print("adding ...")
    elif user_choice == "d":
        print("deleting ...")
    elif user_choice == "s":
        print("showing inventory")
        for num,prod in enumerate(inventory):
            print(f"    {num + 1}.{prod}")
    else:
        print("exiting")
        exit(1)