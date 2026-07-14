def Add(a, b): return a+b

def Subtract(a, b): return a -b

def Multiply(a, b): return a*b

def Divide(a, b):
    if b == 0:
        return 0
    else:
        return a/b

    
def main():
    first = input("Provide First number: ")
    second = input("Provide Second Number: ")

    operator_list = ["+", "-", "/", "*"]
    print(operator_list, end=" ")
    
    key = input(f"\nchose an operator: ")
    functions = [Add, Subtract, Divide, Multiply]

    

   

       


main()

