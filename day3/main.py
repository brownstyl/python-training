def configure_ai_agent(agent_name, *tags, **settings):
    print(f"Agent Name: {agent_name}")
    print(f"Tags: {tags}")
    print(f"Settings: {settings}")

# Calling the function
configure_ai_agent("ChatBot", "support", "nlp", temperature=0.2, streaming=True)

print()

ai_model = {
    "name": "Ghatgpt",
    "version": 2,
    "score": [0.45, 0.23, 0.45, 0.32]
}

sep = ai_model["score"]
print(sep)
ai_model["version"] = 3
ai_model["status"]= "Active"
print(ai_model)

print()

#====== using the list comprehension way to change the list=====#
cal = [1, 2, 3]

new_cal = [x *100 for x in cal]
print(new_cal)

#======using a normal loop for adding or changing the list value======#
old_list = [1, 2, 3]

new_list = []
for x in old_list:
    new_list.append(x*100)
print(new_list)