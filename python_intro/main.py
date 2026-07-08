def add(a, b):
    return a+b

def small_letter(input: str) -> str:
    rawbyte = bytearray(input.encode('ascii'))

    for i in range(len(rawbyte)):
        if 65 <= rawbyte[i] <= 90:
            rawbyte[i] += 32
    return rawbyte.decode('ascii')

for i in range(65, 123):
   if i >= 91 and i <= 96:
        continue
   print(chr(i), end=" ")


def greet(name):
    print()
    print("Good-morning:---", name)
       
       
def subtract(a, b):
    return a-b

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_positive(number):
    return number > 0


def main():
    res = subtract(10, 3)
    print(res)

    pre = is_even(2)   
    print(pre)

    positive = is_positive(4)
    print(positive)



greet("Brownstyl")
print(small_letter("HELLO WORLD"))
print(add(2,4))
main()


