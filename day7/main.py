def greet(text: str):
    return text + "! good morning"

def shout(text: str):
    return text + "... welcome back"

def reverse(text: str):
    return text[::-1]

op = {
    "greet": greet,
    "shout": shout,
    "reverse": reverse
}

def run():
   
    try:
        note = input("enter (continue) to proceed else enter (exit) to terminate: ")
        

        print()
        while note.lower() == "continue":

            mode = input("input a mode: ")
            text = input("input text: ") 
            print()
            return op[mode](text)
        
    
        else:
            while True:
                if note.lower() != "continue" or "exit":
                    print("you can only select from the available option (continue or exit) only")
                    break
                else:
                    if note.lower() == "exit":
                        print("thank you for banking with us...")
                        exit()
        
    
    except KeyError:
        print(f"the key {mode} doesn't exist, please try again...")


print("=============call back function test============")
print(run())