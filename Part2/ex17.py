adjectives = ["Sly", "Stealthy", "Clever", "Mysterious", "Shadowy", "Quick"]
animals = ["Panther","Eagle", "Fox", "Wofl", "Viper", "Hawk"]

user_name = input("Greetings, agent. What is your name?")

import random
random_adjective = random.choice (adjectives)
random_animal = random.choice (animals)
codename = f"{random_adjective} {random_animal}"
lucky_number = random.randint(1, 99)

print(f"Welcome, Agent {user_name}!")
print(f"Your assigned codename is: {codename}")
print(f"And your lucky number for this mission is: {lucky_number}")