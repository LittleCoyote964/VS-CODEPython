#import menu
import lab15

while True:
    lab15.display_loginmenu()
    choice = input("Please input: ")

    if choice == "1":
        lab15.display_login()
        user_id = input("Please input your ID: ")
        user_pwd = input("Please input your password: ")

        idfile = open("id.txt", "r")
        ids = [line.strip() for line in idfile]
        idfile.close()

        pwdfile = open("pass.txt", "r")
        pwds = [line.strip() for line in pwdfile]
        pwdfile.close()

        if user_id in ids:
            index = ids.index(user_id)

            if index < len(pwds) and pwds[index] == user_pwd:
                print("\nLogin has been successful!\n")
                import menu
                menu.run_main_program()
            else:
                print("\nIncorrect password!")
        else:
            print("\nUser not found!")       
         

    elif choice == "2":
        lab15.display_signup()
    
        new_id = input("\nPlease input an ID: ")
        new_pwd = input("Please input a password: ")
    
        idfile = open("id.txt", "a")
        idfile.write(new_id + "\n")
        idfile.close()
    
   
        pwdfile = open("pass.txt", "a")
        pwdfile.write(new_pwd + "\n")
        pwdfile.close()
    
        print("\nSignup has been successful!")
        
    elif choice == "3":
        break

    else:
        choice = input("That is not in the list, press any key to continue. ")
        
