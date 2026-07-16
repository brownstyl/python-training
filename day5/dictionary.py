#==========converting from dictionary to list============#

student_details = {
    "name": "Gabriel odeh",
    "age": 20,
    "class": "primary 2",
    "grade": 200
}

list_storage = list(student_details.items())
print(list_storage)

for key, value in student_details.items():
   # print(key, value)
	list_storage.append([key, value])
#print(list_storage)

print("==================================================================")

# ==================converting list to dictionary ===================#
storage = [['name', 'Gabriel odeh'], ['age', 20], ['class', 'primary 2'], ['grade', 200]]

dic_convo = dict(storage)
print(dic_convo)
#=========================================================================#
print("=====================================================================")

user = {}
if "name" not in user:	

	user["name"] = []
user["name"].append("alice")

print(user)

print("==========================================================")

#when i tried using the format i know from go-lang to impliment here the first one failed and said i should be
#to import a default library which i should import the default dictionary library....
from collections import defaultdict

my_string = "the name of my school is leefcenter"

my_map= defaultdict(int)

for char in my_string:
	my_map[char] += 1
	
for key, value in my_map.items():
	print(key, "--", value)

