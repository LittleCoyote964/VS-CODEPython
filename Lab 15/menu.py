import lab15

while True: 
    lab15.display_menu()
    uc = input("Please input: ")
    if uc == "4":
        break
    elif uc == "1":
        while True:
            lab15.display_utility()
            uc = input("Please input: ")
            if uc == "4":
                break

    elif uc == "2":
        while True:
            lab15.display_game()
            uc = input("Please input: ")
            if uc == "3":
                break
            
    elif uc == "3":
        while True:
            lab15.display_media()
            uc = input("Please input: ")
            if uc == "4":
                break
