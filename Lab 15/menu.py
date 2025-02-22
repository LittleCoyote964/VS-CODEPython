import lab15

while True: 
    lab15.display_menu()
    uc = input("Please input: ")
    if uc == "4":
        break
    elif uc == "1":
        while True:
            lab15.display_utility()
            uc = input("\nPlease input: ")
            if uc == "1" or uc == "2" or uc == "3":
                uc = input("\nI am sorry, it is not ready yet.\n")
                break
            elif uc == "4":
                break
            else:
                uc = input("\nI am sorry, please input correctly:")

    elif uc == "2":
        while True:
            lab15.display_game()
            uc = input("\nPlease input: ")
            if uc == "3":
                break
            elif uc == "2" or uc == "1":
                uc = input("\nI am sorry, it is not ready yet.\n")
            else:
                uc = input("\nI am sorry, please input correctly:")
            
    elif uc == "3":
        while True:
            lab15.display_media()
            uc = input("\nPlease input: ")
            if uc == "4":
                break
            elif uc == "1" or uc == "2" or uc == "3":
                print("\nI am sorry, it is not ready yet.\n")
                break
            else:
                input("\nI am sorry, please input correctly:")
