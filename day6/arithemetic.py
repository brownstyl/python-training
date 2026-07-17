multiiplication = []

for n in range(13):
  multiiplication.append(n * n)

print(multiiplication)

print("=================================================")

print("==================comprehesion Dictionary============used by snr.devs")
num = [n*n for n in range(13)]
print(num)

squares_dict = {n: n*n for n in range(5)}     # {0:0, 1:1, 2:4, 3:9, 4:16}
evens_set = {n for n in range(20) if n % 2 == 0}

print(squares_dict)
print(evens_set)
print("============================================")

#test 1
list_os_cubes = [n**3 for n in range(1, 11)]
print(list_os_cubes)

#test 2
even_numbers = [n for n in range(1,31) if n % 2 == 0]
print(even_numbers)

#test 3
list_of_items = ["go", "python", "ai"]
dic_len = {n: len(n) for n in list_of_items if len(n) > 0}

print(dic_len)

#test 4

words = ["cat", "car", "dog", "duck", "cow"]

first_letter = {w[0] for w in words}

print(first_letter)

print("=================================================")
print("============callback registery================")
#piece 1#

def shout(text: str):
  return text.upper()+"!"

def whisper(text: str):
  return text.lower()+"..."

def reverse(text: str):
  return text[::-1]

#piece 2#
commands = {
  "shout": shout,
  "whisper": whisper,
  "reverse": reverse
}

#piece 3#
def run(command: str, text: str)-> str:
   
    try:
      return commands[command](text)
    except KeyError:
      print(F"your command '{command}' is invalid")
      return
    

print(run("whisper", "hello"))
print(run("s", "hello"))
print(run("reverse", "hello"))