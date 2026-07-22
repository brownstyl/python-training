#what is fibonance??
# fibonance is simply the addition of a two preceeding numbers together and it usually stats at 0 and 1.
#for you to be able to get the next number you must first add the two number directly before it to get the next number.

#implimentation of fibonance takes different methods.... (the tmp local variable, list form, using recursion, and solving it normal way.)

def fibonance_tester(num: int):
    a = 0
    b = 1

    lst = []
    for _ in range(num):
        lst.append(a)
        a, b = b, a + b
    return lst

print(fibonance_tester(5))

# second method using normal method together with a tmp

def fib_tester(n):
    a = 0
    b = 1

    for _ in range(n):
        print(a, end=" ")
        temp = a
        a = b
        b = temp + b
    return n

print(fib_tester(5))

