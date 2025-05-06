def chatbot():
    name = input("Please Enter your name: ")
    print(f"Hello {name}!!   Welcome to Shopify!!")
    print("How can I help You Today!!")
    print("Type 'exit' to end the chat.")

    while True:
        user_input  = input("--->  ")

        if user_input == "exit":
            print("ShopBot: Thank you for visiting. Have a great day!")
            break

        elif "order" in user_input and "status" in user_input:
            print("ShopBot: Please provide your order ID to check the status.")

        elif "store" in user_input and "hours" in user_input:
            print("ShopBot: Our store is open from 9 AM to 9 PM, Monday to Saturday.")

        elif "return" in user_input:
            print("ShopBot: You can return any item within 7 days with the invoice.")

        elif "products" in user_input or "available" in user_input:
            print("ShopBot: We offer electronics, clothing, and home appliances. What are you looking for?")

        elif "hello" in user_input or "hi" in user_input:
            print("ShopBot: Hello! How can I help you today?")

        else:
            print("ShopBot: I'm sorry, I didn't understand that. Can you please rephrase?")

chatbot()