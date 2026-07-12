import time

def password():
    correct_pass = "brown"
    count = 0

    while True:
        user_input = input("please enter your password: ")

        if user_input == correct_pass:
            print("Successfully logged into your account!!...")
            break
           
        else:
            print("Oops incorrect Password Please Retry")
          

            count += 1
            if count == 3:
                print(f"you have entered password for {count} times now!! \nplease wait for 2 mins and try again later")

                time.sleep(10)
                count = 0
                print(f"\nyou can now try {count} times again\n")
                

password()