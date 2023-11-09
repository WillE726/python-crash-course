banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user} you can post a response if you want.")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40 

print(f"your admission cost is ${price}.")

