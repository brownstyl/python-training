developer_details = {
    "name": "Brown",
    "age": 25,
    "favourite_language": "English",
    "expr_yr": "2years",
    "current_learn": "python",
}
 
details = developer_details

print(f"My Name Is {details["name"]}, And I Am {details["age"]}years old, which my favorite language is {details["favourite_language"]}, also i have {details["expr_yr"]} of experience, and i'm currently learning {details["current_learn"]}.")

#=================student data=============#

student_details = {
    "name": "",
    "age": 0, 
    "class": "",
}

name = student_details["name"] = "odeh gabriel"
age = student_details["age"] =20
student_class = student_details["class"] = "primary 4"

print(student_details)

del(student_details["age"])
print(student_details)

print()
def reverse_string():
    s = "hello"
    # Your code here
    st = s.encode('ascii')
    res = bytearray()

    for i in st:
        res.insert(0, i)
      
    return res.decode('ascii')
    
print(reverse_string())


s = "hello"

def reverse_robust_string(s: str) -> str:
    return s[::-1]

w = "hello"

print(reverse_robust_string(w))


#==========deciding a palindrom========#

def palindrome(s: str) -> bool:
    x = 0
    y = len(s)-1
    w = s.lower()

    while x < y:
        if w[x] == " ":
            x += 1
            continue
        if w[y] == " ":
            y -= 1
            continue

        if w[x] != w[y]:
            return False
        x += 1
        y -= 1
    return True

def main():
    st = "M ada      m"
    print(palindrome(st))

main()
print()

#======reversing sentence======#

def reverse_sentence(s: str) -> str:
    res = ""
    for char in s:
        if char in [",", "!", "@",":", ";"]:
            continue
        res += char

    char = res.split()
    print(char)
    reverse = char[::-1]

    return " ".join(reverse)

   


print(reverse_sentence("the! , sky is blue"))