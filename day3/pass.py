import time
import getpass

def password():
    correct_pass = "brown"
    count = 0

    while True:
        user_input = getpass.getpass("please enter your password: ")

        if user_input == correct_pass:
            print("Successfully logged into your account!!...")
            break
           
        else:
            print("Oops incorrect Password Please Retry")
          

            count += 1
            if count == 3:
                print()
                print("=====Notice=====")
                print(f"you have entered password for {count} times now!! \nplease wait for 2 sec and try again later")

                time.sleep(3)
                count = 0
                print("\nyou can now try 3 times again\n")
                

password()