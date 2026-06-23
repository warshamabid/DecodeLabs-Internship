print("Welcome to online store chatbot!")
name=input("before we start, what's your name?")
print(f"Hello {name}!, How can I assist you?")
while True:
    user = input("\nYou: ").lower()
    if user in["hi","hello","hey"]:
        print(f"Bot: hello{name}! Welcome to our online store .")
    elif user=="products":
         print("Bot: We offer Electronics, Clothing, Shoes and Accessories.")

    elif user == "payment":

        print("Bot: Available payment methods are:")
        print("- Credit Card")
        print("- Debit Card")
        print("- PayPal")
        print("- Bank Transfer")

    elif user == "shipping":

        print("Bot: Standard shipping takes 3-5 business days.")

    elif user == "order status":

        order_id = input("Enter your Order ID: ")

        if order_id == "1001":
            print("Bot: Your order has been Delivered.")

        elif order_id == "1002":
            print("Bot: Your order is Out for Delivery.")

        elif order_id == "1003":
            print("Bot: Your order is Being Processed.")

        else:
            print("Bot: Sorry, Order ID not found.")

    elif user == "help":

        print("\nAvailable Commands:")
        print("hello")
        print("products")
        print("payment")
        print("shipping")
        print("order status")
        print("help")
        print("bye")

    elif user in ["bye", "exit", "quit"]:

        print(f"Bot: Thank you for visiting our store, {name}.")
        print("Bot: Have a great day!")
        break

    else:

        print("Bot: Sorry, I didn't understand that.")
        print("Bot: Type 'help' to see available commands.")