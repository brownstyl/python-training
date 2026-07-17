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
list_os_cubes = [n**3 for n in range(1, 10)]
print(list_os_cubes)

#test 2
even_numbers = [n for n in range(1,32) if n % 2 == 0]
print(even_numbers)

#test 3
list_of_items = ["go", "python", "ai"]
dic_len = {len(n):[n] for n in list_of_items if len(n) > 0}

print(dic_len)




example2 = list_of_items
print(example2)

pri = {
  2: ['go', 'ai'],
  6: ['python']
}

adder = {}

for n in pri:
  if len(n) > 0:
    adder[len(n)].append(n)

print(adder)

#test 4
